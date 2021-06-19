from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('addtoreserv/<int:id>/<slug:slug>', views.addtoreserv, name='addtoreserv'),
    path('deletereservcart/<int:id>', views.deletereservcart, name='deletereservcart'),
    path('reservcart', views.reservcart, name='reservcart'),
    path('reservit', views.reservit, name='reservit')
]