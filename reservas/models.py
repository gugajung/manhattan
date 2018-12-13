from django.db import models
import datetime
from apartamentos.models import Apartamentos

# Create your models here.




class Reservation(models.Model):
    room = models.ForeignKey(Apartamentos, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)
    start_date = models.DateField(null=False, verbose_name='start of reservation')
    #end_date = models.DateField(null=False, default=now, verbose_name='end of reservation')
    end_date = models.DateField(null=False, verbose_name='end of reservation')
    valor_diaria = models.DecimalField(max_digits=6, decimal_places=2)
    valor_pago = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def total(self):
        date1 = self.end_date
        date2 = self.start_date
        dias = abs((date1 - date2).days)
        print(dias)
        return self.valor_diaria * dias

    def saldo(self):
        x = self.total - self.valor_pago
        return str(x)

    def __str__(self):
        return 'Apartamento: ' + str(self.room) + ' - Check in: ' + str(self.start_date) + ' - Saldo a pagar: ' + self.saldo + " " + self.total

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

