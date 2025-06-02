from django.urls import path
from .views import UserPostListView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    like_post,
)
from . import views

urlpatterns = [
    path('',
         PostListView.as_view(),
         name='blog-home'),
    path('post/<int:pk>/',
         PostDetailView.as_view(),
         name='post-detail'),
    path('post/new/',
         PostCreateView.as_view(),
         name='post-create'),
    path(
        'post/<int:pk>/update/',
        PostUpdateView.as_view(),
        name='post-update'
    ),
    path(
        'post/<int:pk>/delete/',
        PostDeleteView.as_view(),
        name='post-delete'
    ),
    path(
        'post/<int:pk>/like/',
        like_post,
        name='like-post'
    ),
    path(
        'about/',
        views.about,
        name='blog-about'
    ),
    path(
        'user/<str:username>/',
        UserPostListView.as_view(),
        name='user-posts'
    ),

    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter')

]
