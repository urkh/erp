from django.db import models

class Articulos(models.Model):
    nombre = models.TextField()
    existencia = models.IntegerField()
    medidas = models.TextField()

    def __unicode__(self):
        return self.nombre

