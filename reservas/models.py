from django.db import models
from apartamentos.models import Apartamentos

# Create your models here.




class Reservation(models.Model):
    room = models.ForeignKey(Apartamentos, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)
    start_date = models.DateField(null=False,
                                  verbose_name='start of reservation')
    #end_date = models.DateField(null=False, default=now, verbose_name='end of reservation')
    end_date = models.DateField(null=False,
                                verbose_name='end of reservation')