from draft.utils.constants_util import Role
from draft.utils.exception_util import BusinessException
from draft.utils.log_util import get_logger
from draft.utils.public_util import hash_encryption
from market.models.models import User

logger = get_logger("user")


class UserModel(object):

    def register(self, username, password, nickname, gender, phone):
        # 判断用户是否存在
        if User.objects.filter(username=username).exists():
            raise BusinessException("用户名{}已存在".format(username))
        # 密码加密存储
        password = hash_encryption(password)
        # 保存用户信息
        add_params = {
            "username": username,
            "password": password,
            "nickname": nickname,
            "gander": gender,
            "phone": phone,
            "role": Role.general.value,
        }
        logger.info("注册用户信息：{}".format(add_params))
        user = User(**add_params)
        user.save()
        logger.info("注册用户成功：{}".format(username))

