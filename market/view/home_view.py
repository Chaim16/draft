import random

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from draft import settings
from draft.utils.log_util import get_logger
from draft.utils.response import setResult
from draft.utils.validate import TransCoding
from market.service.home_model import HomeModel
from market.view.serilazer import CrawlerSerializer

logger = get_logger("home")


class HomeViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(methods=['GET'], detail=False)
    @swagger_auto_schema(
        operation_description="随机获取轮播图",
        manual_parameters=[
            openapi.Parameter("number", openapi.IN_QUERY, description="数量", type=openapi.TYPE_NUMBER)
        ],
        tags=["首页"],
    )
    def crawler(self, request):
        """随机取5个url"""
        params = TransCoding().transcoding_dict(dict(request.GET.items()))
        number = int(params.get("number", 5))
        home_model = HomeModel()
        data = home_model.crawler(number)
        return setResult(data)
