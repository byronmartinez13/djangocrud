from django.contrib import admin
from django.urls import path, include
from empleados.views_vbf import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('vbf/', include('empleados.urls_vbf')),
    path('vbc/', include('empleados.urls_vbc')),
]
