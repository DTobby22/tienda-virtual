from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "TiendaVirtualApp/home.html")

def servicios(request):
    return render(request, "TiendaVirtualApp/servicios.html")

def tienda(request):
    return render(request, "TiendaVirtualApp/tienda.html")

def blog(request):
    return render(request, "TiendaVirtualApp/blog.html")

def contacto(request):
    return render(request, "TiendaVirtualApp/contacto.html")