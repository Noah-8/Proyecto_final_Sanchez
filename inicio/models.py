from django.db import models

# Create your models here.

class Teclado(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    fecha_publicacion = models.DateField()