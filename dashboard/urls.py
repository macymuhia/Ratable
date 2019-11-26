from django.urls import path
from django.conf import settings
from dashboard import views

urlpatterns = [
# <<<<<<< HEAD
#     path("dashboard/", views.dashboard, name="dashboard"),
# =======
    path("", views.index, name="dashboard-index"),
    path("landing_page/", views.landing_page_view, name="landing_page"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
# >>>>>>> develop
]
