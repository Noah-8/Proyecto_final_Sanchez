from django import forms

class PublicarTecladoFormulario(forms.Form):
    modelo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    fecha_publicacion = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=('%d/%m/%Y', ))
    descripcion = forms.CharField(max_length=1000)
    autor = forms.CharField(max_length=20)
    imagen = forms.ImageField()
    

class BusquedaTecladoFormulario(forms.Form):
    modelo = forms.CharField(max_length=20, required=False)