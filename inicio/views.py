from django.shortcuts import render
from inicio.forms import PublicarTecladoFormulario, BusquedaTecladoFormulario
from inicio.models import Teclado

from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

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

def listar_teclados(request):
    
    formulario = BusquedaTecladoFormulario(request.GET)
    if formulario.is_valid():
        modelo_a_buscar = formulario.cleaned_data.get('modelo', '')
        lista_teclados = Teclado.objects.filter(modelo__icontains=modelo_a_buscar)
    
    formulario = BusquedaTecladoFormulario()
    return render(request, 'inicio/teclados.html', {'formulario': formulario, 'lista_teclados': lista_teclados})

class DetalleTeclado(DetailView):
    model = Teclado
    template_name = "inicio/detalle_teclado.html"
    
class ModificarTeclado(UpdateView):
    model = Teclado
    fields = ['modelo', 'marca']
    template_name = "inicio/modificar_teclado.html"
    success_url = reverse_lazy('inicio:teclados')


class EliminarTeclado(DeleteView):
    model = Teclado
    template_name = "inicio/eliminar_teclado.html"
    success_url = reverse_lazy('inicio:teclados')
