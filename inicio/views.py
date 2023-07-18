from django.shortcuts import render, redirect
from inicio.forms import PublicarTecladoFormulario, BusquedaTecladoFormulario
from inicio.models import Teclado
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

@login_required
def publicar_teclado(request):
    if request.method == 'POST':
        formulario = PublicarTecladoFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            teclado = Teclado(modelo=info['modelo'], marca=info['marca'], fecha_publicacion=info['fecha_publicacion'], descripcion=info['descripcion'], autor=info['autor'], imagen=info['imagen'])
            teclado.save()
            return redirect('inicio:teclados')
        else:
            return render(request, 'inicio/publicar_teclado.html', {'formulario': formulario})
    
    formulario = PublicarTecladoFormulario()
    return render(request, 'inicio/publicar_teclado.html', {'formulario': formulario})

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
    
class ModificarTeclado(LoginRequiredMixin, UpdateView):
    model = Teclado
    fields = ['modelo', 'marca', 'descripcion']
    template_name = "inicio/modificar_teclado.html"
    success_url = reverse_lazy('inicio:teclados')


class EliminarTeclado(LoginRequiredMixin, DeleteView):
    model = Teclado
    template_name = "inicio/eliminar_teclado.html"
    success_url = reverse_lazy('inicio:teclados')
    
def about(request):
    return render(request, 'inicio/about.html')

def paginas(request):
    return render(request, 'inicio/paginas.html')
