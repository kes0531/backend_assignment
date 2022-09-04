from django.urls import path
from .views import UserProfileAPI, UserSignupAPI

urlpatterns = [
    path("user/<str:name>", UserProfileAPI.as_view()),
    path("signup/", UserSignupAPI.as_view()),
]