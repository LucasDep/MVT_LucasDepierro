from msilib.schema import Class
from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    edad=models.IntegerField()
    fechaNac=models.DateTimeField()