from django.db import models

# Create your models here.

class Articulos(models.Model):
    nombre = models.TextField()
    existencia = models.IntegerField()
    medidas = models.TextField()

    def __unicode__(self):
        return self.nombre

