from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactformMessage


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'note', 'subject', 'status']
    list_filter = ['status']


admin.site.register(ContactformMessage, ContactFormMessageAdmin)
admin.site.register(Setting)
