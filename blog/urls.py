from django.urls import path
from . import views

urlpatterns = [
    path('create-post/', views.CreatePost.as_view()),
    path('posts/', views.ListPosts.as_view()),


    path('create-comment/', views.CreateComment.as_view()),
]
