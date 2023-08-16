from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    return render(request, "vehiculos/home.html")

def autos(request):
    contexto = {'autos': Autos.objects.all() }
    return render(request, "vehiculos/autos.html", contexto)

def camionetas(request):
    contexto = {'camionetas': Camionetas.objects.all() }
    return render(request, "vehiculos/camionetas.html", contexto)

def motos(request):
    contexto = {'motos': Motos.objects.all() }
    return render(request, "vehiculos/motos.html", contexto)

def autosForm(request):
    if request.method == "POST":
        miForm = AutosForm(request.POST)
        if miForm.is_valid():
            autos_marca = miForm.cleaned_data.get('marca')
            autos_modelo = miForm.cleaned_data.get('modelo')
            autos_color = miForm.cleaned_data.get('color')
            autos_precio = miForm.cleaned_data.get('precio')
            autos = Autos(marca=autos_marca,
                          modelo=autos_modelo,
                          color=autos_color,
                          precio=autos_precio)
            autos.save()
            return render(request, "vehiculos/base.html")
    else:
        miForm = AutosForm()

    return render(request, "vehiculos/autosForm.html", {"form": miForm})

def camionetasForm(request):
    if request.method == "POST":
        miForm = CamionetasForm(request.POST)
        if miForm.is_valid():
            camionetas_marca = miForm.cleaned_data.get('marca')
            camionetas_modelo = miForm.cleaned_data.get('modelo')
            camionetas_color = miForm.cleaned_data.get('color')
            camionetas_precio = miForm.cleaned_data.get('precio')
            camionetas = Camionetas(marca=camionetas_marca,
                          modelo=camionetas_modelo,
                          color=camionetas_color,
                          precio=camionetas_precio)
            camionetas.save()
            return render(request, "vehiculos/base.html")
    else:
        miForm = CamionetasForm()

    return render(request, "vehiculos/camionetasForm.html", {"form": miForm})

def motosForm(request):
    if request.method == "POST":
        miForm = MotosForm(request.POST)
        if miForm.is_valid():
            motos_marca = miForm.cleaned_data.get('marca')
            motos_modelo = miForm.cleaned_data.get('modelo')
            motos_color = miForm.cleaned_data.get('color')
            motos_precio = miForm.cleaned_data.get('precio')
            motos = Motos(marca=motos_marca,
                          modelo=motos_modelo,
                          color=motos_color,
                          precio=motos_precio)
            motos.save()
            return render(request, "vehiculos/base.html")
    else:
        miForm = MotosForm()

    return render(request, "vehiculos/motosForm.html", {"form": miForm})

def buscarAutos(request):
    return render(request, "vehiculos/buscarAutos.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        autos = Autos.objects.filter(marca__icontains=patron)
        contexto = {"autos": autos}
        return render(request, "vehiculos/autos.html", contexto)
    return HttpResponse("Usted no Ingreso Ningun Dato a Buscar")