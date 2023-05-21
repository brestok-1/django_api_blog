from rest_framework.routers import DefaultRouter

from accounts.views import UsersViewSet

router = DefaultRouter()
router.register('', UsersViewSet, basename='users')

urlpatterns = [] + router.urls
