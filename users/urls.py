from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.users, name="users"),
    path("profile", views.profile, name="profile"),
    path("", LoginView.as_view(), {
         "next_page": settings.LOGIN_REDIRECT_URL}, name="login",),
    path("logout/", LogoutView.as_view(),
         {"next_page": settings.LOGOUT_REDIRECT_URL}, name="logout",),
]
