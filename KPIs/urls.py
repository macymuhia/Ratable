from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


# from django.urls import path, include

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('score/',views.score,name='score'),
    path('area/new/', views.new_area, name='new_area'),
    path('areas',views.areas, name='areas'),
    path('indicator/new/', views.new_indicator, name='new_indicator'),
    path('score/new',views.new_score,name='new_score'),
]
