from django.urls import path
from KPIs import views

urlpatterns = [
    path("dashboard/kpis/", views.kpis, name="kpis"),
    path("dashboard/reports/", views.reports, name="reports"),
    path("dashboard/kpis/comments/", views.comments, name="comments"),
]
