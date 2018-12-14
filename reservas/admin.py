from django.contrib import admin
from .models import Reservation, Mensalista, MovMensalista

# Register your models here.

admin.site.register(Reservation)
admin.site.register(Mensalista)
admin.site.register(MovMensalista)

