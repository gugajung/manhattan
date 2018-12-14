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

    from datetime import date

    def diffDate(self, data1, data2):
        d1 = data1
        d2 = data2
        delta = d2 - d1
        r = delta.days if (delta.days > 0) else "erro"
        return r

    def total_diarias(self, dias, valordiara):
        dia = dias
        valor = valordiara
        valor_total = valor * dia
        return valor_total

    def saldo(self, pg, total):
        pago = pg
        total = total
        saldo = total - pago
        return saldo

    def __str__(self):
        return ('Apartamento: ' + str(self.room) +
                ' - Check in: ' + str(self.start_date) +
                ' - Check out: ' + str(self.end_date) +
                ' - diárias: ' + str(self.diffDate(self.start_date, self.end_date)) +
                ' - Valor Total: ' + str(self.total_diarias(self.diffDate(self.start_date, self.end_date), self.valor_diaria)) +
                ' - Saldo: ' + str(self.saldo(self.valor_pago, self.total_diarias(self.diffDate(self.start_date, self.end_date), self.valor_diaria)))

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
    valor_devido = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    valor_mensalidade = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    valor_Luz = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.mensalista)
