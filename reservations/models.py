from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm

from transfer.models import Transfer


class Reservation(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=155, blank=True)
    city = models.CharField(max_length=30, blank=True)
    pickup = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(max_length=20, blank=True)
    adminnote = models.CharField(blank=True, max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


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
        return str(self.transfer)


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'address', 'pickup', 'phone', 'city', ]
