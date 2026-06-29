from django.shortcuts import render, get_object_or_404, redirect
from .models import Cargo, Empleado
from .forms import CargoForm, EmpleadoForm


def home(request):
    total_cargos = Cargo.objects.count()
    total_empleados = Empleado.objects.count()
    return render(request, 'empleados/home.html', {
        'total_cargos': total_cargos,
        'total_empleados': total_empleados,
    })


# ─────────────────────────────────────────────
#  CRUD Cargos — Vistas Basadas en Funciones
# ─────────────────────────────────────────────

def cargo_lista_vbf(request):
    cargos = Cargo.objects.all()
    return render(request, 'empleados/vbf/cargo_lista.html', {'cargos': cargos})


def cargo_crear_vbf(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vbf:cargo_lista')
    else:
        form = CargoForm()
    return render(request, 'empleados/vbf/cargo_form.html', {
        'form': form,
        'titulo': 'Registrar Cargo',
        'accion': 'Guardar',
    })


def cargo_editar_vbf(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('vbf:cargo_lista')
    else:
        form = CargoForm(instance=cargo)
    return render(request, 'empleados/vbf/cargo_form.html', {
        'form': form,
        'titulo': 'Editar Cargo',
        'accion': 'Actualizar',
    })


def cargo_eliminar_vbf(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        cargo.delete()
        return redirect('vbf:cargo_lista')
    return render(request, 'empleados/vbf/cargo_confirmar_eliminar.html', {'cargo': cargo})


# ─────────────────────────────────────────────
#  CRUD Empleados — Vistas Basadas en Funciones
# ─────────────────────────────────────────────

def empleado_lista_vbf(request):
    empleados = Empleado.objects.select_related('cargo').all()
    return render(request, 'empleados/vbf/empleado_lista.html', {'empleados': empleados})


def empleado_crear_vbf(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vbf:empleado_lista')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/vbf/empleado_form.html', {
        'form': form,
        'titulo': 'Registrar Empleado',
        'accion': 'Guardar',
    })


def empleado_editar_vbf(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('vbf:empleado_lista')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/vbf/empleado_form.html', {
        'form': form,
        'titulo': 'Editar Empleado',
        'accion': 'Actualizar',
    })


def empleado_eliminar_vbf(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('vbf:empleado_lista')
    return render(request, 'empleados/vbf/empleado_confirmar_eliminar.html', {'empleado': empleado})
