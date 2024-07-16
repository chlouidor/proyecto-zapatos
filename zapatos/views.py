from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from zapatos.models import Usuario
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm
from django.db import IntegrityError
 
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
        if request.method == 'GET':
            return render(request,'registration/registrar.html',{
                'form':UserCreationForm
            })
        else:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user= User.objects.create_user(
                        username=request.POST['username'],
                        password=request.POST['password1']
                        )
                    user.save()
                    login (request,user)
                    return redirect('iniciar_sesion')
                except IntegrityError:
                     return render(request,'registration/registrar.html',{
                'form':UserCreationForm,
                'error' : 'La cuenta ya existe'
                })
            else:
                return render(request,'registration/registrar.html',{
                'form':UserCreationForm,
                'error' : 'Las contraseñas no coinciden'
                })
                
def ver_dat(request):
    usuarios=Usuario.objects.all()
    return render(request,'registration/ver_datos.html',{
        'usuarios':usuarios
    })



def agregar_datos(request):
    if request.method != "POST":
        return render(request,"registration/agregar_datos.html")
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
        context = { "mensaje": "Sus datos han sido agregados" }
        return render(request,"core/index.html",context)


def actualizar_datos(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        fechaNac = request.POST["fechaNac"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]


        usuario = Usuario()
        usuario.rut = rut
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.fecha_nacimiento = fechaNac
        usuario.telefono = telefono
        usuario.email = email
        usuario.direccion = direccion
        usuario.activo = 1

        usuario.save()
        context = {"mensaje":"Datos actualizados satisfactoriamente","usuario":usuario}
        return render(request,"registration/act_datos.html",context)
    else:
        usuarios = Usuario.objects.all
        context = {"usuarios":usuarios}
        return render(request,"registration/ver_datos.html",context) 

def borrar_datos(request,pk):
    context= {}
    try:
        usuario = Usuario.objects.get(rut=pk)
        usuario.delete()

        mensaje = "datos eliminado"
        usuarios = Usuario.objects.all()
        context = {"usuarios":usuarios,"mensaje":mensaje}
        return render(request,"registration/ver_datos.html",context)
    except:
        mensaje = "Error al eliminar"
        usuarios = Usuario.objects.all()
        context = {"usuarios":usuario,"mensaje":mensaje}
        return render(request,"registration/ver_datos.html",context)           

def usuarios_findEdit(request,pk):
    
    if pk != "":
        usuario = Usuario.objects.get(rut=pk)

        context = {"usuario":usuario}

        if usuario:
            return render(request,"registration/act_datos.html",context)
        else:
            context = {"mensaje":"Error , el rut no existe"}
            return render(request,"registration/ver_datos.html",context)


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


