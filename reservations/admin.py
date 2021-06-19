from django.contrib import admin

# Register your models here.
from reservations.models import Reservation, reservTransfer, ReservCart


class ReservationCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'transfer', ]
    list_filter = ['user']


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'status', 'pickup']
    list_filter = ['status']
    readonly_fields = ('user', 'address', 'city', 'first_name', 'last_name', 'phone', 'status', 'pickup')


class ReservationTransferAdmin(admin.ModelAdmin):
    list_display = ['user', 'transfer', 'price']
    list_filter = ['user']


admin.site.register(ReservCart, ReservationCartAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(reservTransfer, ReservationTransferAdmin)
