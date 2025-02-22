from rest_framework.routers import DefaultRouter

from market.view.home_view import HomeViewSet
from market.view.user_view import UserViewSet

router = DefaultRouter()

urlpatterns = []
router.register(r'api/v1/user', UserViewSet, basename="user")
router.register(r'api/v1/home', HomeViewSet, basename="home")
urlpatterns += router.urls
