from django.shortcuts import render
from ServiciosApp.models import Servicio

# Create your views here.

def home(request):
    return render(request, "TiendaVirtualApp/home.html")

def servicios(request):
    servicio = Servicio.objects.all()
    return render(request, "TiendaVirtualApp/servicios.html", {"servicios": servicio})

def tienda(request):
    return render(request, "TiendaVirtualApp/tienda.html")

def blog(request):
    return render(request, "TiendaVirtualApp/blog.html")

def contacto(request):
    return render(request, "TiendaVirtualApp/contacto.html")