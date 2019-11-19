# from django.urls import path
# from . import views

# urlpatterns = [
#     path("dashboard/departments/", views.departments, name="departments"),
   
from django.urls import path, include
from django.conf import settings
from Departments import views

urlpatterns = [                                             path("dashboard/departments/", views.departments, name="departments"),
    path('add_department/', views.add_department_view, name='add_department'),
]
