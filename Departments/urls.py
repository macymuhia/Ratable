from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path("", views.department_list_view, name='department_list'),
    path('create/', views.department_create_view,
         name='department_create'),
    # path('add_department/', views.add_department_view, name='add_department'),
    path('search/', views.search, name='search'),

]
