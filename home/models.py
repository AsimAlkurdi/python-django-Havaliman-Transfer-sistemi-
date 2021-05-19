from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.

from django.forms import ModelForm, TextInput, Textarea



class Setting(models.Model):
    STATUS = (
        ('True', 'YES'),
        ('False', 'NO'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=20)
    smtppassword = models.CharField(blank=True, max_length=10)
    smtpport = models.CharField(blank=True, max_length=6)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=150)
    instagram = models.CharField(blank=True, max_length=150)
    twitter = models.CharField(blank=True, max_length=150)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactformMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(max_length=50, blank=False)
    message = models.CharField(blank=False, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default="New")
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactformMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'name-input', 'placeholder': 'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'name-input', 'placeholder': 'Subject'}),
            'email': TextInput(attrs={'class': 'name-input', 'placeholder': 'Email Address'}),
            'message': Textarea(attrs={'class': 'name-input', 'placeholder': 'Your Message', 'row': '5'}),
        }
