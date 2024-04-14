from django.urls import path
from . import views

urlpatterns = [
    path('create-post/', views.CreatePost.as_view()),
    path('posts/', views.ListPosts.as_view()),
    path('posts/<int:pk>/update/', views.UpdatePost.as_view()),
    path('posts/<int:pk>/delete/', views.DeletePost.as_view()),


    path('create-comment/', views.CreateComment.as_view()),
    path('comments/<int:pk>/update/', views.UpdateComment.as_view(), name='update_comment'),
    path('comments/<int:pk>/delete/', views.DestroyComment.as_view()),
]
