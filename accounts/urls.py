from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
]

app_name = "accounts"