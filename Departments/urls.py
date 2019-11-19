from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('department-edit/', views.edit_deparments, name='department-edit'),
    path('searchresult/', views.searchresult,name='searchresult'),
    path("", views.list_departments_view, name="list_departments"),
    path('add_department/', views.add_department_view, name='add_department'),
    path('search/', views.search, name='search'),
    
        
]
