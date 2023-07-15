from django.db import models

# Create your models here.

class Teclado(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    fecha_publicacion = models.DateField()
    descripcion = models.TextField(null=True)
    autor = models.CharField(max_length=20, default='')
    imagen = models.ImageField(upload_to='fotos_teclados', null=True, blank=True)
    
    def __str__(self):
        return f'Modelo: {self.modelo} - Marca: {self.marca}'