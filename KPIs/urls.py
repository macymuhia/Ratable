from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('area/new/', views.new_area, name='new_area'),
    path('indicator/new/', views.new_indicator, name='new_indicator'),
    path("reports/", views.score_reports, name="reports"),
    path("average/", views.area_report, name="averages"),


    path("dashboard/kpis/", views.kpis, name="kpis"),
    path("dashboard/reports/", views.reports, name="reports"),
    path("dashboard/kpis/comments/", views.comments, name="comments"),
    # urlpatterns=[
    #     path('',views.welcome,name = 'welcome'),
    #     path('score/',views.score,name='score'),
    #     path('area/new/', views.new_area, name='new_area'),
    #     path('areas',views.areas, name='areas'),
    #     path('indicator/new/', views.new_indicator, name='new_indicator'),
    #     path('score/new',views.new_score,name='new_score'),
    #     path("kpis", views.kpis, name="kpis"),
    #     path("dashboard/reports/", views.reports, name="reports"),
    #     path("dashboard/kpis/comments/", views.comments, name="comments")
    path('score/', views.score, name='score'),
    path('areas', views.areas, name='areas'),
    path('score/new', views.new_score, name='new_score'),
    path("kpis", views.kpis, name="kpis"),
    path("comments", views.comments, name="comments"),
]
