from django.urls import path,include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('department-edit/', views.edit_deparments, name='department-edit'),
    path('searchresult/', views.searchresult,name='searchresult'),
    
    
        
]