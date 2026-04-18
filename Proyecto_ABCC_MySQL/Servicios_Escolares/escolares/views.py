from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Alumno
from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

#---ALTAS
class CrearAlumno(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Alumno 
    form = Alumno
    fields = "__all__"
    success_message = "Alumno AGREGADO con EXITO"


    def get_success_url(self):
        return reverse('listar')

#---BAJAS
class EliminarAlumno(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Alumno
    form = Alumno
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Alumno eliminado correctamente!!!'
        messages.success(self.request, success_message)
        return reverse('listar')
    

#-- Cambios

class ActualizarAlumno(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Alumno 
    form = Alumno
    fields = "__all__"
    success_message = "Alumno MODIFICADO con EXITO"


    def get_success_url(self):
        return reverse('listar')
    

#COnsultas


class DetalleAlumno( LoginRequiredMixin,DetailView):
    model = Alumno

class ListarAlumnos(LoginRequiredMixin, ListView):
        model = Alumno 

# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/alumnos') 
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'alumnos/login.html')

# REGISTRO
def registro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password != confirm:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('registro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return redirect('registro')

        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, 'Usuario creado correctamente')
        return redirect('login')

    return render(request, 'alumnos/registro.html')
# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')



