from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from home.models import UserProfile


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'name-input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'name-input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'name-input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'name-input', 'placeholder': 'last_name'}),

        }


CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'name-input', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'name-input', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'name-input', 'placeholder': 'city'}, choices=CITY),
            'country': TextInput(attrs={'class': 'name-input', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'name-input', 'placeholder': 'image'}),

        }


LOCATION = [
    ('Address', 'Address'),
    ('Hotel', 'Hotel'),
]
BAGGAGE = [
    ('YES', 'YES'),
    ('NO', 'NO')
]
STATUS = [
    ('New', 'New'),
    ('Accepted', 'Accepted'),
    ('Canceled', 'Canceled'),
]
