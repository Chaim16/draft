from rest_framework_simplejwt.tokens import RefreshToken

from draft.utils.constants_util import Role
from draft.utils.exception_util import BusinessException
from draft.utils.log_util import get_logger
from market.models import User

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
            "role": Role.general.value,
        }
        logger.info("注册用户信息：{}".format(add_params))
        User.objects.create_user(**add_params)
        logger.info("注册用户成功：{}".format(username))

    def whoami(self, username):
        # 判断用户是否存在
        if not User.objects.filter(username=username).exists():
            raise BusinessException("用户名{}不存在".format(username))

        user = User.objects.get(username=username)
        return {
            "username": user.username,
            "role": user.role,
        }

