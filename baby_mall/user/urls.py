from django.urls import path
from .views import UserProfileAPI, UserSignupAPI, UserLoginAPI

urlpatterns = [
    path("user/<str:userid>/", UserProfileAPI.as_view()),
    path("user/signup/", UserSignupAPI.as_view()),
    path("user/login/", UserLoginAPI.as_view()),
]