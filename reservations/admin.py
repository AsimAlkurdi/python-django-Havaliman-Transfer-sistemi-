from django.contrib import admin

# Register your models here.
from reservations.models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'pickup']
    list_filter = ['last_name']


admin.site.register(Reservation, ReservationAdmin)
