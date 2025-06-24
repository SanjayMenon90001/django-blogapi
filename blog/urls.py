from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet

# Main router for posts
router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet, basename='comment')

urlpatterns = [
     # Make sure this line is present!
    path("", include(router.urls)),
]
