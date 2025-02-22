import random

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action

from draft import settings
from draft.utils.log_util import get_logger
from draft.utils.response import setResult

logger = get_logger("home")


class HomeViewSet(viewsets.ViewSet):

    @action(methods=['GET'], detail=False)
    @swagger_auto_schema(
        operation_description="随机获取一张轮播图",
        tags=["首页"],
    )
    def crawler(self, request):
        url = settings.STATIC_URL + "image_{}.jpg".format(random.randint(1, 10))
        return setResult({
            "url": url
        })
