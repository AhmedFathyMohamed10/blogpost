from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('users/', views.GetUsers.as_view(), name='users')
]
