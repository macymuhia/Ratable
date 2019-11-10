from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from django.conf import settings

urlpatterns = [
    path("", LoginView.as_view(), {
         "next_page": settings.LOGIN_REDIRECT_URL}, name="login",),
    path("logout/", LogoutView.as_view(),
         {"next_page": settings.LOGOUT_REDIRECT_URL}, name="logout",),
]
