from django.db import models
from clientes.models import Juridica
# Create your models here.

class Hotel(models.Model):
    name = models.ForeignKey(Juridica, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Apartamentos(models.Model):
    numero_apto = models.IntegerField()
    ramal = models.IntegerField()
    pertence = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.numero_apto)

