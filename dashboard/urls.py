from django.urls import path
from django.conf import settings
from dashboard import views

urlpatterns = [
    path("", views.index, name="dashboard-index"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
