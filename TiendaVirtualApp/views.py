from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "TiendaVirtualApp/home.html")

def tienda(request):
    return render(request, "TiendaVirtualApp/tienda.html")

