from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers as nested_routers

from .views import CommentViewSet, PostViewSet

# Main router for posts
router = DefaultRouter()
router.register(r"posts", PostViewSet)

# Nested router for comments under posts
posts_router = nested_routers.NestedDefaultRouter(router, r"posts", lookup="post")
posts_router.register(r"comments", CommentViewSet, basename="post-comments")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(posts_router.urls)),
]

from .views import AdminAuthorPostSummary

urlpatterns += [
    path('api/admin/posts/comments/', AdminAuthorPostSummary.as_view(), name='admin-post-comments'),
]
# This adds the URL for the admin summary view