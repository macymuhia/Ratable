from django.urls import path
from KPIs import views

urlpatterns = [
    path("", views.kpis, name="kpis"),
    path("", views.graphs, name="graphs"),
]
