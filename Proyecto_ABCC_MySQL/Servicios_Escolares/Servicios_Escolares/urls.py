"""
URL configuration for Servicios_Escolares project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from escolares.views import *
from escolares import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', views.login_view),

    path('alumnos/', ListarAlumnos.as_view(template_name= "alumnos/index.html"), name='listar'), 
    path('alumnos/detalle/<int:pk>', DetalleAlumno.as_view(template_name= "alumnos/detalle.html"), name='detalle'), 
    path('alumnos/crear', CrearAlumno.as_view(template_name= "alumnos/crear.html"), name='crear'), 
    path('alumnos/eliminar/<int:pk>', EliminarAlumno.as_view(), name='eliminar'), 
    path('alumnos/editar/<int:pk>', ActualizarAlumno.as_view(template_name= "alumnos/editar.html"), name='editar'), 
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),
]
