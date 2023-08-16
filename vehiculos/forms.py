from django import forms

class AutosForm(forms.Form):
    marca = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    color = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)

class CamionetasForm(forms.Form):
    marca = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    color = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)

class MotosForm(forms.Form):
    marca = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    color = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)