from django.urls import path, include, re_path
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from . import views

urlpatterns = [
    # path("users", views.users, name="users"),
    # path("profile", views.profile, name="profile"),
    # path("", views.adduser, name="adduser"),
    # path("login", views.login, name="login"),
    path("", views.login_user, name="login",),
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
    path('group_create/', views.group_create_view, name='create_group'),
    path('group_list/', views.group_list_view, name='create_list'),
    path('add_user/', views.add_user_view, name='add_user'),
    path("account_activation_sent/", views.account_activation_sent,
         name="account_activation_sent"),
    re_path(
        r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$", views.activate, name="activate"),

]
