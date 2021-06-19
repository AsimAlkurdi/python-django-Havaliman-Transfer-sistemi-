from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm

from transfer.models import Transfer


class Reservation(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )

    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=155)
    city = models.CharField(max_length=30)
    pickup = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    image = models.ImageField(blank=True, upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


class reservTransfer(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.transfer.title


class ReservCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    transfer = models.ForeignKey(Transfer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.transfer


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'address', 'pickup', 'phone', 'city', ]
