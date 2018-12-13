from django.db import models
from clientes.models import Juridica
# Create your models here.

class Hotel(models.Model):
    name = models.ForeignKey(Juridica, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    tag = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.tag


class Apartamentos(models.Model):
    numero_apto = models.IntegerField(unique=True)
    ramal = models.IntegerField(blank=True, null=True)
    pertence = models.ForeignKey(Hotel, on_delete=models.PROTECT)
    tag = models.ForeignKey(Tag,on_delete=models.PROTECT, blank=True, null=True )

    def __str__(self):
        return str(self.numero_apto)

    class Meta:
        verbose_name = "Apartamento"
        verbose_name_plural = "Apartamentos"

