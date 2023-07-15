from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('paginas/', views.paginas, name='paginas'),
    path('teclados/', views.listar_teclados, name='teclados'),
    path('teclados/<int:pk>/', views.DetalleTeclado.as_view(), name='detalle_teclado'),
    path('teclados/<int:pk>/modificar/', views.ModificarTeclado.as_view(), name='modificar_teclado'),
    path('teclados/<int:pk>/eliminar/', views.EliminarTeclado.as_view(), name='eliminar_teclado'),
    path('teclados/publicar/', views.publicar_teclado, name='publicar_teclado'),
]
