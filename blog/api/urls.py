from rest_framework import routers
from .views import UserModelViewSet, BlogModelViewSet, CommentModelViewSet
router = routers.DefaultRouter()
router.register("users", UserModelViewSet)
router.register("blogs", BlogModelViewSet)
router.register("comments", CommentModelViewSet)
urlpatterns = []
urlpatterns.extend(router.urls)
