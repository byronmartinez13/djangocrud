from django import forms
from .models import Cargo, Empleado


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del cargo'
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción (opcional)'
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
        }


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombres', 'apellidos', 'correo', 'sueldo', 'fecha_ingreso', 'cargo']
        widgets = {
            'nombres': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombres del empleado'
            }),
            'apellidos': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellidos del empleado'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'sueldo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01'
            }),
            'fecha_ingreso': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'cargo': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'correo': 'Correo Electrónico',
            'sueldo': 'Sueldo ($)',
            'fecha_ingreso': 'Fecha de Ingreso',
            'cargo': 'Cargo',
        }
