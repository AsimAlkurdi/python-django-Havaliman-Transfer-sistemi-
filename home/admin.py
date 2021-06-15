from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactformMessage, UserProfile


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'note', 'subject', 'status']
    list_filter = ['status']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'address', 'city', 'country', 'image_tag']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ContactformMessage, ContactFormMessageAdmin)
admin.site.register(Setting)
