from django.shortcuts import render
from inicio.forms import PublicarTecladoFormulario
from inicio.models import Teclado

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def publicar_teclado(request):
    mensaje = ''
    if request.method == 'POST':
        formulario = PublicarTecladoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            teclado = Teclado(modelo=info['modelo'], marca=info['marca'], fecha_publicacion=info['fecha_publicacion'])
            teclado.save()
            mensaje = f'Se publico el teclado {teclado.marca} {teclado.modelo}'
        else:
            return render(request, 'inicio/publicar_teclado.html', {'formulario': formulario})
    
    formulario = PublicarTecladoFormulario()
    return render(request, 'inicio/publicar_teclado.html', {'formulario': formulario, 'mensaje': mensaje})