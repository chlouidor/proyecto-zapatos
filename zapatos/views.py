from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from zapatos.models import Usuario
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm
 
# Create your views here.

@login_required
def compras(request):
    return render(request,'core/compras.html')


def inicio(request):
    
    return render(request,"core/index.html")


def zapatos_hombre(request):
    return render(request,'core/zapatos_hombre.html')


def zapatos_mujer(request):
    return render(request,'core/zapatos_mujer.html')

def registrar(request):
    if request.method != "POST":
        return render(request,"registration/registrar.html")
    else:

        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        fechaNac = request.POST["fechaNac"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        obj = Usuario.objects.create(
            rut = rut,
            nombre = nombre,
            apellido = apellido,
            fecha_nacimiento = fechaNac,
            telefono = telefono,
            email = email,
            direccion = direccion,
            activo=1
        )
        obj.save()
        context = { "mensaje": "Su cuenta Ha sido creada" }
        return render(request,"registration/login.html",context)

            


def iniciar_sesion(request):
    
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)  
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.error(request, "Cuenta invalida")
        else:
            messages.error(request, "Datos incorrectos")    
    
    return render(request, "registration/login.html", {"form": form})

def proximo(request):
    return render(request,'zap/proximos.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def pago_completado(request):
    return render(request,'core/Pago-Completado.html')

def salir(request):
    logout (request)
    return redirect('inicio')


