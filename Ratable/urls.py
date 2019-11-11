from django.contrib import admin 
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin', include('users.urls')),
    path('dashboard', include('dashboard.urls')),
    path('', include('kpis.urls')),
]
