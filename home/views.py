from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactformMessage, ContactForm
from transfer.models import Category, Transfer, Images


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    daytransfer = Transfer.objects.all()[:4]
    lasttransfer = Transfer.objects.all().order_by('-id')[:4]
    context = {'setting': setting, 'category': category, 'daytransfer': daytransfer, 'lasttransfer': lasttransfer, }
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category, }
    return render(request, 'aboutus.html/', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting
        , 'category': category}
    return render(request, 'references.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactformMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your Message sent successfully.")
            return HttpResponseRedirect('/contact')
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm()
    context = {'setting': setting, 'form': form,
               'category': category, }
    return render(request, 'contact.html', context)


def category_transfer(request, id, slug):
    categorydata = Category.objects.get(pk=id)
    category = Category.objects.all()
    transfer = Transfer.objects.filter(category_id=id, status='True')
    context = {'transfer': transfer,
               'category': category,
               'categorydata': categorydata}
    return render(request, 'transfer.html', context)


def transfer_detail(request, id, slug):
    category = Category.objects.all()
    images = Images.objects.filter(transfer_id=id)
    transfer = Transfer.objects.get(pk=id)
    context = {'category': category, 'transfer': transfer, 'images': images}
    return render(request, 'transfer_detail.html', context)
