from rest_framework import routers

from django.urls import include, path

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='Post')
router.register(r'groups', GroupViewSet, basename='Group')
router.register(r'follow', FollowViewSet, basename='Follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='Comment'
)

urlpatterns = [
    path('v1/', include(router.urls), name='api-root'),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
