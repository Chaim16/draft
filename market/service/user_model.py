import time
from turtledemo.bytedesign import Designer

from django.forms import model_to_dict

from draft.utils.constants_util import Role, DesignerApplicationStatus
from draft.utils.exception_util import BusinessException
from draft.utils.log_util import get_logger
from market.models import User, DesignerApplicationRecord

logger = get_logger("user")


class UserModel(object):

    def register(self, username, password, nickname, gender, phone):
        # 判断用户是否存在
        if User.objects.filter(username=username).exists():
            raise BusinessException("用户名{}已存在".format(username))

        # 保存用户信息
        add_params = {
            "username": username,
            "password": password,
            "nickname": nickname,
            "gender": gender,
            "phone": phone,
            "role": Role.GENERAL.value,
        }
        logger.info("注册用户信息：{}".format(add_params))
        User.objects.create_user(**add_params)
        logger.info("注册用户成功：{}".format(username))

    def whoami(self, username):
        user = User.objects.get(username=username)
        return {
            "username": user.username,
            "role": user.role,
        }

    def detail(self, username):
        user = User.objects.get(username=username)
        user_dict = {
            "username": user.username,
            "nickname": user.nickname,
            "gender": user.gender,
            "phone": user.phone,
            "role": user.role,
            "balance": user.balance,
        }
        return user_dict

    def modify(self, username, nickname, gender, phone, role):

        modify_params = {}
        if nickname:
            modify_params["nickname"] = nickname
        if gender is not None:
            modify_params["gender"] = gender
        if phone:
            modify_params["phone"] = phone
        if role:
            modify_params["role"] = role
        logger.info("修改用户信息：{}".format(modify_params))
        User.objects.filter(username=username).update(**modify_params)

    def id_by_username(self, username):
        user = User.objects.get(username=username)
        return user.id

    def designer_application_record(self, username):
        user_id = self.id_by_username(username)
        record = DesignerApplicationRecord.objects.filter(user_id=user_id)
        if not record.exists():
            return {}
        record = record.first()
        record_dict = model_to_dict(record)
        return record_dict

    def apply_as_designer(self, username, reason):
        user_id = self.id_by_username(username)
        params = {
            "user_id": user_id,
            "reason": reason,
            "status": DesignerApplicationStatus.WAIT_APPROVAL.value,
            "create_time": int(time.time()),
        }
        record = DesignerApplicationRecord.objects.create(**params)
        return {"id": record.id}


