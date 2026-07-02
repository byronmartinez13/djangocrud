from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def _con_estilo_bootstrap(form):
    for field in form.fields.values():
        field.widget.attrs.setdefault('class', 'form-control')
    return form


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('gestion_empleados')
    else:
        form = UserCreationForm()
    return render(request, 'empleados/signup.html', {'form': _con_estilo_bootstrap(form)})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('gestion_empleados')
    else:
        form = AuthenticationForm()
    return render(request, 'empleados/signin.html', {'form': _con_estilo_bootstrap(form)})


@login_required
def signout(request):
    logout(request)
    return redirect('home')
