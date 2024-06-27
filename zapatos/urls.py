
from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('zapatos_hombre/',views.zapatos_hombre, name='zapatos_hombre'),
    path('zapatos_mujer/',views.zapatos_mujer, name='zapatos_mujer'),
    path('login/',views.login, name='login'),
    path('salir',views.salir, name='salir'),
    path('nosotros/',views.nosotros, name='nosotros'),

    path('compras/',views.compras, name='compras'),

   
]
