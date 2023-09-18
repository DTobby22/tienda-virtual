from django.shortcuts import render, redirect
from .forms import FormContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto = FormContacto()

    if request.method == 'POST':
        formulario_contacto = FormContacto(data=request.POST)
        
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            email = EmailMessage("Mensaje enviado de la app web", 
                                 "El usuario {} con la direccion {} escribe: \n\n {}".format(nombre, email, contenido),
                                 "", ["micorreo@gmail.com"], reply_to=[email])

            try:
                email.send()

                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/=novalido')


    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})

