from django.urls import path
from django.views.i18n import JavaScriptCatalog

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservationdetails/<int:id>', views.reservationdetails, name='reservationdetails'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
]
