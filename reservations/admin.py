from django.contrib import admin

# Register your models here.
from reservations.models import Reservation, reservTransfer


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'status', 'pickup']
    list_filter = ['status']


class ReservationTransferAdmin(admin.ModelAdmin):
    list_display = ['title', 'reservation', 'price']
    list_filter = ['status']


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(reservTransfer, ReservationTransferAdmin)
