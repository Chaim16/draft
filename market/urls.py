from rest_framework.routers import DefaultRouter

from market.views.user_view import UserViewSet

router = DefaultRouter()

urlpatterns = []
router.register(r'api/v1/user', UserViewSet, basename="user")
urlpatterns += router.urls
