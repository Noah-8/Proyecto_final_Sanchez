from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('teclados/publicar/', views.publicar_teclado, name='publicar_teclado'),
]
