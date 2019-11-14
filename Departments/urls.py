from django.urls import path, include
from django.conf import settings
from Departments import views

urlpatterns = [
    path('add_department/', views.add_department_view, name='add_department'),
]