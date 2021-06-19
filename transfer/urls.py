
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from home import views

urlpatterns = [

    path('', views.index, name='index'),
]
