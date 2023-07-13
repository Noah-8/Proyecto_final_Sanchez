from django import forms

class PublicarTecladoFormulario(forms.Form):
    modelo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    fecha_publicacion = forms.DateField()
    