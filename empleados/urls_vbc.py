from django.urls import path
from . import views_vbc

app_name = 'vbc'

urlpatterns = [
    # Cargos
    path('cargos/', views_vbc.CargoListView.as_view(), name='cargo_lista'),
    path('cargos/crear/', views_vbc.CargoCreateView.as_view(), name='cargo_crear'),
    path('cargos/<int:pk>/editar/', views_vbc.CargoUpdateView.as_view(), name='cargo_editar'),
    path('cargos/<int:pk>/eliminar/', views_vbc.CargoDeleteView.as_view(), name='cargo_eliminar'),
    # Empleados
    path('empleados/', views_vbc.EmpleadoListView.as_view(), name='empleado_lista'),
    path('empleados/crear/', views_vbc.EmpleadoCreateView.as_view(), name='empleado_crear'),
    path('empleados/<int:pk>/editar/', views_vbc.EmpleadoUpdateView.as_view(), name='empleado_editar'),
    path('empleados/<int:pk>/eliminar/', views_vbc.EmpleadoDeleteView.as_view(), name='empleado_eliminar'),
]
