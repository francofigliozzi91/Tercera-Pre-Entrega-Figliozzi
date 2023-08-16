from django.urls import path, include
from .views import*

urlpatterns = [
    path('', home, name="home" ),
    path('autos/', autos, name="autos" ),
    path('camionetas/', camionetas, name="camionetas" ),
    path('motos/', motos, name="motos" ),

    path('autos_form', autosForm, name="autos_form" ),
    path('camionetas_form', camionetasForm, name="camionetas_form" ),
    path('motos_form', motosForm, name="motos_form" ),

    path('buscar_autos/', buscarAutos, name="buscar_autos" ),
    path('buscar2/', buscar2, name="buscar2" ),
]