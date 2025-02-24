import random
import traceback

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from draft.utils.constants_util import Role
from draft.utils.exception_util import BusinessException
from draft.utils.log_util import get_logger
from draft.utils.response import setResult
from draft.utils.validate import TransCoding
from market.service.draft_model import DraftModel
from market.service.user_model import UserModel
from market.view.serilazer import PublishDraftSerializer

logger = get_logger("home")


class DraftViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(methods=['POST'], detail=False)
    @swagger_auto_schema(
        operation_description="发布画稿",
        request_body=PublishDraftSerializer,
        tags=["画稿中心"],
    )
    def publish(self, request):
        user = request.user
        if not user.is_authenticated:
            return setResult({}, "用户未登录", 1)

        params = request.POST
        logger.info(request.FILES)
        logger.info(type(request.FILES))

        image = request.FILES.get("image", "")
        title = params.get("title", "")
        description = params.get("description", "")
        price = params.get("price", "")
        category_id = params.get("category_id", "")

        user_model = UserModel()
        draft_model = DraftModel()
        try:
            username = user.username
            user_dict = user_model.detail(username)
            if user_dict.get('role') == Role.GENERAL.value:
                raise BusinessException("权限不足")
            data = draft_model.publish(title, description, image, price, category_id, username)
            return setResult(data)
        except Exception as e:
            logger.error("发布画稿失败：{}".format(traceback.format_exc()))
            raise BusinessException("发布画稿失败")

