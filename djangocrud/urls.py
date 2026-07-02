from django.contrib import admin
from django.urls import path, include
from empleados.views_vbf import home, gestion_empleados, modulo_empleados, modulo_cargos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('gestion/', gestion_empleados, name='gestion_empleados'),
    path('gestion/empleados/', modulo_empleados, name='modulo_empleados'),
    path('gestion/cargos/', modulo_cargos, name='modulo_cargos'),
    path('', include('empleados.urls_auth')),
    path('vbf/', include('empleados.urls_vbf')),
    path('vbc/', include('empleados.urls_vbc')),
]
