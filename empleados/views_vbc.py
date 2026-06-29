from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cargo, Empleado
from .forms import CargoForm, EmpleadoForm


# ─────────────────────────────────────────────
#  CRUD Cargos — Vistas Basadas en Clases
# ─────────────────────────────────────────────

class CargoListView(ListView):
    model = Cargo
    template_name = 'empleados/vbc/cargo_lista.html'
    context_object_name = 'cargos'


class CargoCreateView(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'empleados/vbc/cargo_form.html'
    success_url = reverse_lazy('vbc:cargo_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar Cargo'
        context['accion'] = 'Guardar'
        return context


class CargoUpdateView(UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'empleados/vbc/cargo_form.html'
    success_url = reverse_lazy('vbc:cargo_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cargo'
        context['accion'] = 'Actualizar'
        return context


class CargoDeleteView(DeleteView):
    model = Cargo
    template_name = 'empleados/vbc/cargo_confirmar_eliminar.html'
    success_url = reverse_lazy('vbc:cargo_lista')
    context_object_name = 'cargo'


# ─────────────────────────────────────────────
#  CRUD Empleados — Vistas Basadas en Clases
# ─────────────────────────────────────────────

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleados/vbc/empleado_lista.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        return Empleado.objects.select_related('cargo').all()


class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/vbc/empleado_form.html'
    success_url = reverse_lazy('vbc:empleado_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar Empleado'
        context['accion'] = 'Guardar'
        return context


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/vbc/empleado_form.html'
    success_url = reverse_lazy('vbc:empleado_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Empleado'
        context['accion'] = 'Actualizar'
        return context


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleados/vbc/empleado_confirmar_eliminar.html'
    success_url = reverse_lazy('vbc:empleado_lista')
    context_object_name = 'empleado'
