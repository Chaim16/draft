import json
import traceback

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action

from draft.utils.constants_util import Role
from draft.utils.exception_util import BusinessException, ParamsException
from draft.utils.log_util import get_logger
from draft.utils.response import setResult
from draft.utils.validate import TransCoding
from market.service.alipay_model import AlipayModel
from market.service.user_model import UserModel
from market.view.serilazer import RegisterSerializer, UserModifySerializer, ApplyAsDesignerSerializer, \
    RechargeSerializer, ApproveDesignerApplicationSerializer, UserDeleteSerializer

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
        gender = params.get('gender')
        phone = params.get('phone')
        nickname = params.get('nickname')

        if password != confirm_password:
            raise BusinessException("两次密码不一致")

        user_model = UserModel()
        user_model.register(username, password, nickname, gender, phone)
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


    @action(methods=['GET'], detail=False)
    @swagger_auto_schema(
        operation_description="detail",
        tags=["用户管理"],
    )
    def user_detail(self, request):
        user = request.user
        if not user.is_authenticated:
            return setResult({}, "用户未登录", 1)
        user_model = UserModel()
        data = user_model.detail(user.username)
        return setResult(data)

    @action(methods=['POST'], detail=False)
    @swagger_auto_schema(
        operation_description="编辑用户信息",
        request_body=UserModifySerializer,
        tags=['用户管理']
    )
    def modify(self, request):
        serializer = UserModifySerializer(data=request.data)
        if not serializer.is_valid():
            raise ParamsException(str(serializer.errors))
        user = request.user
        if not user.is_authenticated:
            return setResult({}, "用户未登录", 1)

        params = json.loads(request.body)

        if not params.get('username') or user.username == params.get('username'):
            username = user.username
        else:
            if user.role != Role.ADMINISTRATOR.value:
                raise BusinessException("只能修改自己的信息")
            username = params.get('username')
        nickname = params.get('nickname')
        gender = params.get('gender')
        phone = params.get('phone')
        role = params.get('role')

        user_model = UserModel()
        try:
            user_model.modify(username, nickname, gender, phone, role)
            return setResult()
        except Exception as e:
            logger.error("修改用户信息失败：{}".format(traceback.format_exc()))
            raise BusinessException("修改用户信息失败")

    @action(methods=['GET'], detail=False)
    @swagger_auto_schema(
        operation_description="申请设计师记录",
        tags=["用户管理"],
    )
    def designer_application_record(self, request):
        user = request.user
        if not user.is_authenticated:
            return setResult({}, "用户未登录", 1)

        username = user.username
        user_model = UserModel()
        try:
            data = user_model.designer_application_record(username)
            return setResult(data)
        except Exception as e:
            logger.error("获取设计师申请记录失败：{}".format(traceback.format_exc()))
            raise BusinessException("获取设计师申请记录失败")

    @action(methods=['POST'], detail=False)
    @swagger_auto_schema(
        operation_description="申请成为设计师",
        request_body=ApplyAsDesignerSerializer,
        tags=['用户管理']
    )
    def apply_as_designer(self, request):
        user = request.user
        if not user.is_authenticated:
            return setResult({}, "用户未登录", 1)

        params = json.loads(request.body)
        reason = params.get('reason')
        username = user.username
        user_model = UserModel()
        try:
            data = user_model.apply_as_designer(username, reason)
            return setResult(data)
        except Exception as e:
            logger.error("申请成为设计师失败：{}".format(traceback.format_exc()))
            raise BusinessException("申请成为设计师失败")

    @action(methods=['POST'], detail=False)
    @swagger_auto_schema(
        operation_description="充值",
        request_body=RechargeSerializer,
        tags=['用户管理']
    )
    def recharge(self, request):
        user = request.user
        if not user.is_authenticated:
            return setResult({}, "用户未登录", 1)
        params = json.loads(request.body)
        amount = params.get('amount')
        username = user.username

        user_model = UserModel()
        try:
            data = user_model.recharge(username, amount)
            return setResult(data)
        except Exception as e:
            logger.error("创建充值订单失败：{}".format(traceback.format_exc()))
            raise BusinessException("创建充值订单失败")

    @action(methods=['GET'], detail=False)
    @swagger_auto_schema(
        operation_description="获取申请设计师列表",
        tags=["用户管理"],
    )
    def apply_designer_list(self, request):
        user = request.user
        if not user.is_authenticated:
            return setResult({}, "用户未登录", 1)

        params = TransCoding().transcoding_dict(dict(request.GET.items()))
        page = int(params.get('page', 1))
        size = int(params.get('size', 10))
        user_model = UserModel()
        try:
            username = user.username
            user_dict = user_model.detail(username)
            if user_dict.get('role') != Role.ADMINISTRATOR.value:
                raise BusinessException("权限不足")
            data = user_model.apply_designer_list(page, size)
            return setResult(data)
        except Exception as e:
            logger.error("获取申请设计师列表失败：{}".format(traceback.format_exc()))
            raise BusinessException("获取申请设计师列表失败")

    @action(methods=['POST'], detail=False)
    @swagger_auto_schema(
        operation_description="充值",
        request_body=ApproveDesignerApplicationSerializer,
        tags=['用户管理']
    )
    def approve_designer_application(self, request):
        user = request.user
        if not user.is_authenticated:
            return setResult({}, "用户未登录", 1)

        params = json.loads(request.body)
        record_id = params.get('record_id')
        status = params.get('status')
        approval_opinions = params.get('approval_opinions')
        user_model = UserModel()
        try:
            username = user.username
            user_dict = user_model.detail(username)
            if user_dict.get('role') != Role.ADMINISTRATOR.value:
                raise BusinessException("权限不足")
            user_model.approve_designer_application(record_id, status, approval_opinions)
            return setResult()
        except Exception as e:
            logger.error("审批设计师申请失败：{}".format(traceback.format_exc()))
            raise BusinessException("审批设计师申请失败")

    @action(methods=['GET'], detail=False)
    @swagger_auto_schema(
        operation_description="用户列表",
        request_body=ApproveDesignerApplicationSerializer,
        tags=['用户管理']
    )
    def user_list(self, request):
        user = request.user
        if not user.is_authenticated:
            return setResult({}, "用户未登录", 1)

        params = TransCoding().transcoding_dict(dict(request.GET.items()))
        page = int(params.get('page', 1))
        size = int(params.get('size', 10))
        user_model = UserModel()
        try:
            username = user.username
            user_dict = user_model.detail(username)
            if user_dict.get('role') != Role.ADMINISTRATOR.value:
                raise BusinessException("权限不足")
            data = user_model.user_list(page, size)
            return setResult(data)
        except Exception as e:
            logger.error("获取用户列表失败：{}".format(traceback.format_exc()))
            raise BusinessException("获取用户列表失败")

    @action(methods=['POST'], detail=False)
    @swagger_auto_schema(
        operation_description="删除用户",
        request_body=UserDeleteSerializer,
        tags=['用户管理']
    )
    def del_user(self, request):
        user = request.user
        if not user.is_authenticated:
            return setResult({}, "用户未登录", 1)

        params = json.loads(request.body)
        user_model = UserModel()
        try:
            username = user.username
            user_dict = user_model.detail(username)
            if user_dict.get('role') != Role.ADMINISTRATOR.value:
                raise BusinessException("权限不足")
            username = params.get('username')
            user_dict = user_model.detail(username)
            if user_dict.get('role') == Role.ADMINISTRATOR.value:
                raise BusinessException("不能删除管理员账号")

            user_model.del_user(username)
            return setResult()
        except Exception as e:
            logger.error("删除用户失败：{}".format(traceback.format_exc()))
            raise BusinessException("删除用户失败")

