from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = RichTextField(null=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
