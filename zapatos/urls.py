
from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('zapatos_hombre/',views.zapatos_hombre, name='zapatos_hombre'),
    path('zapatos_mujer/',views.zapatos_mujer, name='zapatos_mujer'),
    path('iniciar_sesion/',views.iniciar_sesion, name='iniciar_sesion'),
    path('salir',views.salir, name='salir'),
    path('nosotros/',views.nosotros, name='nosotros'),
    path("registrar/", views.registrar, name="registrar"),
    path("proximo/", views.proximo, name="proximo"),

    path('usuarios_findEdit/<str:pk>', views.usuarios_findEdit, name='usuarios_findEdit'),
    path("agregar_datos/",views.agregar_datos, name='agregar_datos'),
    path("ver_datos/",views.ver_dat, name="ver_dat"),
    path("actualizar_datos/",views.actualizar_datos, name="actualizar_datos"),
    path("eliminar_datos/<str:pk>",views.borrar_datos, name="borrar_datos"),

    path('zapatos_findEdit/<str:pk>', views.zapatos_findEdit, name='zapatos_findEdit'),
    path("agregar_zapatos/",views.agregar_zapatos, name='agregar_zapatos'),
    path("lista_zapatos/",views.lista_zapatos, name="lista_zapatos"),
    path("editar_zapatos/",views.editar_zapatos, name="editar_zapatos"),
    path("borrar_zapatos/<str:pk>",views.borrar_zapatos, name="borrar_zapatos"),

    path('compras/',views.compras, name='compras'),
    path('pago_completado/',views.pago_completado, name='pago_completado'),

   
]
