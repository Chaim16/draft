import json
import traceback

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action

from draft.utils.exception_util import BusinessException, ParamsException
from draft.utils.log_util import get_logger
from draft.utils.response import setResult
from market.service.user_model import UserModel
from market.view.serilazer import RegisterSerializer

logger = get_logger("user")


class UserViewSet(viewsets.ViewSet):

    @action(methods=['POST'], detail=False)
    @swagger_auto_schema(
        operation_description="注册",
        request_body=RegisterSerializer,
        tags=['用户管理']
    )
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            raise ParamsException(str(serializer.errors))
        params = json.loads(request.body)
        username = params.get('username')
        password = params.get('password')
        confirm_password = params.get('confirm_password')
        gander = params.get('gander')
        phone = params.get('phone')
        nickname = params.get('nickname')

        if password != confirm_password:
            raise BusinessException("两次密码不一致")

        user_model = UserModel()
        user_model.register(username, password, nickname, gander, phone)
        return setResult()

    @action(methods=['GET'], detail=False)
    @swagger_auto_schema(
        operation_description="whoami",
        tags=["用户管理"],
    )
    def whoami(self, request):
        user_model = UserModel()
        user = request.user
        if not user.is_authenticated:
            return setResult({}, "用户未登录", 1)
        data = user_model.whoami(user.username)
        return setResult(data)

