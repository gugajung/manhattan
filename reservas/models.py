from django.db import models

# Create your models here.



class Hotel(models.Model):
    #photo = models.ImageField(upload_to=hotel_directory_path,
     #                         default='hotel_minimal_erd.png')
    name = models.CharField(max_length=60, default='', blank=True, null=True)
    address = models.ForeignKey(Address, null=True, blank=True)
    description = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    reservations = models.ManyToManyField(
        User,
        through='Reservation',
        through_fields=('room', 'user'),
    )
    #photo = models.ImageField(upload_to=room_directory_path,
                              #default='hotel_minimal_erd.png')
    hotel = models.ForeignKey(Hotel, null=True, blank=True,
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=60, default='', blank=True, null=True)
    description = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    room = models.ForeignKey(Room, default=None, null=True, blank=True,
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, null=True, blank=True,
                             on_delete=models.CASCADE)
    start_date = models.DateField(null=False, default=now,
                                  verbose_name='start of reservation')
    end_date = models.DateField(null=False, default=now,
                                verbose_name='end of reservation')