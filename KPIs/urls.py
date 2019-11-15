from django.urls import path
from KPIs import views

urlpatterns = [
    path("kpis", views.kpis, name="kpis"),
    path("reports", views.reports, name="reports"),
    path("", views.comments, name="comments"),
]
