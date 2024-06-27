from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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

def login(request):
    return render(request,'core/login.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def pago_completado(request):
    return render(request,'core/pago_completado.html')

def salir(request):
    logout (request)
    return redirect('inicio')


