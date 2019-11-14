from django.urls import path
from . import views

urlpatterns = [
    path("", views.kpis, name="kpis"),
    path("", views.graphs, name="graphs"),
]
