from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from . import views

urlpatterns = [
    path("", LoginView.as_view(), {
         "next_page": settings.LOGIN_REDIRECT_URL}, name="login",),
    path("logout/", LogoutView.as_view(),
         {"next_page": settings.LOGOUT_REDIRECT_URL}, name="logout",),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

]
