from django.urls import path
from .views import *

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="login_url"),
    path('auth/user/me/', UserInfo.as_view(), name="user_info"),
    path('users/', UserListCreateAPIView.as_view()),
    path('users/<str:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),
]
