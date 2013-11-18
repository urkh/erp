from django.db import models

class Clientes(models.Model):
    rif = models.CharField(max_length=50)
    codigo = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    fecha_ing = models.DateField()
    status = models.BooleanField()
    correo = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.TextField()

    def __unicode__(self):
        return self.nombre


"""


class Correos(models.Model):
    clientes = models.ForeignKey(Clientes)
    correo = models.EmailField(max_length=100)

    def __unicode__(self):
        return self.correo


class Telefonos(models.Model):
    clientes = models.ForeignKey(Clientes)
    numero = models.IntegerField()

    def __unicode__(self):
        return self.numero


class Direcciones(models.Model):
    clientes = models.ForeignKey(Clientes)
    direccion = models.TextField()

    def __unicode__(self):
        return self.direccion
"""