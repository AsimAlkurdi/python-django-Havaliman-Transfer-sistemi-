from django.db import models


# Create your models here.


class Reservation(models.Model):
    STATUS = (

        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )

    title = models.CharField(max_length=30)
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
        return self.title


class reservTransfer(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
