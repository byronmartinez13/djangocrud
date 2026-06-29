from django.urls import path
from . import views_vbf

app_name = 'vbf'

urlpatterns = [
    # Cargos
    path('cargos/', views_vbf.cargo_lista_vbf, name='cargo_lista'),
    path('cargos/crear/', views_vbf.cargo_crear_vbf, name='cargo_crear'),
    path('cargos/<int:pk>/editar/', views_vbf.cargo_editar_vbf, name='cargo_editar'),
    path('cargos/<int:pk>/eliminar/', views_vbf.cargo_eliminar_vbf, name='cargo_eliminar'),
    # Empleados
    path('empleados/', views_vbf.empleado_lista_vbf, name='empleado_lista'),
    path('empleados/crear/', views_vbf.empleado_crear_vbf, name='empleado_crear'),
    path('empleados/<int:pk>/editar/', views_vbf.empleado_editar_vbf, name='empleado_editar'),
    path('empleados/<int:pk>/eliminar/', views_vbf.empleado_eliminar_vbf, name='empleado_eliminar'),
]
