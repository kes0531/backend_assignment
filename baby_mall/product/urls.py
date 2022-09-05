from django.urls import path
from .views import ProductAPI, ProductAllAPI, ProductSignupAPI

urlpatterns = [
    path("product/<int:pid>", ProductAPI.as_view()),
    path("product/", ProductAllAPI.as_view()),
    path("product/signup/", ProductSignupAPI.as_view()),
]