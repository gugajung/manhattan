from django.db import models

# Create your models here.
class Apartamentos(models.Model):
    numero_apto = models.IntegerField()
    ramal = models.IntegerField()

    def __str__(self):
        return str(self.numero_apto)

