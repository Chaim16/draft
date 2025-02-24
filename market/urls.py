from rest_framework.routers import DefaultRouter

from market.view.alipay_view import AlipayViewSet
from market.view.draft_view import DraftViewSet
from market.view.home_view import HomeViewSet
from market.view.order_view import OrderViewSet
from market.view.user_view import UserViewSet

router = DefaultRouter()

urlpatterns = []
router.register(r'api/v1/user', UserViewSet, basename="user")
router.register(r'api/v1/home', HomeViewSet, basename="home")
router.register(r'api/v1/alipay', AlipayViewSet, basename="alipay")
router.register(r'api/v1/draft', DraftViewSet, basename="draft")
router.register(r'api/v1/order', OrderViewSet, basename="order")
urlpatterns += router.urls
