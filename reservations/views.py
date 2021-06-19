from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.models import UserProfile
from reservations.models import ReservCart, ReservationForm, Reservation, reservTransfer
from transfer.models import Category, Transfer, Images


# Create your views here.
def index(request):
    return HttpResponse("resavasi page")


@login_required(login_url='/login')
def addtoreserv(request, id, slug):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    if request.method == 'POST':
        data = ReservCart()
        data.user_id = current_user.id
        data.transfer_id = id
        data.save()
        category = Category.objects.all()
        reserv_cart = ReservCart.objects.filter(user_id=current_user.id)
        context = {'category': category, 'reserv_cart': reserv_cart}
        return render(request, 'reserv_cart.html', context)
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def reservcart(request):
    category = Category.objects.all()
    current_user = request.user
    reserv_cart = ReservCart.objects.filter(user_id=current_user.id)
    context = {'category': category, 'reserv_cart': reserv_cart}
    return render(request, 'reserv_cart.html', context)


@login_required(login_url='/login')
def deletereservcart(request, id):
    ReservCart.objects.filter(id=id).delete()
    return HttpResponseRedirect('/')


@login_required(login_url='/login')
def reservit(request):
    category = Category.objects.all()
    current_user = request.user
    reserv_cart = ReservCart.objects.filter(user_id=current_user.id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            data = Reservation()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.pickup = form.cleaned_data['pickup']
            data.user_id = current_user.id
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            reserv_cart = ReservCart.objects.filter(user_id=current_user.id)
            for rs in reserv_cart:
                detail = reservTransfer()
                detail.reservation_id = data.id
                detail.transfer_id = rs.transfer_id
                detail.user_id = current_user.id
                detail.price = rs.transfer.price
                detail.save()
            ReservCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_item'] = 0
            messages.success(request, " your reservation has completed")
            context = {'category': category}
            return render(request, 'reservation_completed.html', context)
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/reservations/reservit')
    form = ReservationForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'reserv_cart': reserv_cart, 'category': category, 'form': form, 'profile': profile, }
    return render(request, 'reservation_form.html', context)
