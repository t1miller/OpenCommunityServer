# users/urls.py
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'following', views.FollowingViewset, basename='Following')
router.register(r'follower', views.FollowerViewset, basename='Follower')
router.register(r'inbox', views.InboxViewset, basename='Inbox')

urlpatterns = [
    path('', include(router.urls)),
    # path('followers/', views.FollowingViewset.as_view()),
    # path('requests/', views.FollowingViewset.as_view()),
    # path('thread/', views.FollowingViewset.as_view())
]
