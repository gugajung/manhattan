from django.db import models
import datetime
from decimal import Decimal

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

    def Calcula(self):
        checkin = datetime.datetime.strptime(self.start_date, "%m/%d/%Y").date()
        checkout = datetime.datetime.strptime(self.end_date, "%m/%d/%Y").date()
        custo = self.valor_diaria
        timedeltaSum = checkout - checkin
        StayDuration = timedeltaSum.days

        TotalCost = StayDuration * 10
        TotalCost = int(TotalCost)
        return TotalCost


    def __str__(self):
        return ('Apartamento: ' + str(self.room) +
                ' - Check in: ' + str(self.start_date) +
                ' - Check out: ' + str(self.Calcula())
        )

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"


class Mensalista(models.Model):
    apto = models.ForeignKey(Apartamentos, on_delete=models.PROTECT)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.apto) + ' - ' + str(self.inicio)


class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.PROTECT)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.mensalista) + ' - ' + str(self.total)