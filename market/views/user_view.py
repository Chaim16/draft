import json
import traceback

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action

from draft.utils.exception_util import BusinessException, ParamsException
from draft.utils.log_util import get_logger
from draft.utils.response import setResult
from market.models.user_model import UserModel
from market.views.serilazer import RegisterSerializer

logger = get_logger("user")


class UserViewSet(viewsets.ViewSet):

    @action(methods=['POST'], detail=False)
    @swagger_auto_schema(
        operation_description="注册",
        request_body=RegisterSerializer,
        tags=['用户管理']
    )
    def register(self, request):
        """注册功能"""
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            raise ParamsException(str(serializer.errors))
        try:
            params = json.loads(request.body)
            username = params.get('username')
            password1 = params.get('password1')
            password2 = params.get('password2')
            gander = params.get('gander')
            phone = params.get('phone')
            nickname = params.get('nickname')

            if password1 != password2:
                raise BusinessException("两次密码不一致")

            user_model = UserModel()
            user_model.register(username, password1, nickname, gander, phone)
            return setResult()
        except Exception as e:
            logger.error("注册用户失败，{}".format(traceback.format_exc()))
            raise BusinessException("注册用户失败")
