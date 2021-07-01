from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.form import SignUpForm
from home.models import Setting, ContactformMessage, ContactForm, UserProfile, FAQ
from transfer.models import Category, Transfer, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    daytransfer = Transfer.objects.all()[:4]
    lasttransfer = Transfer.objects.all().order_by('-id')[:4]
    context = {'setting': setting, 'category': category, 'daytransfer': daytransfer, 'lasttransfer': lasttransfer, }
    return render(request, 'index.html', context)


def aboutus(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'category': category, }
    return render(request, 'aboutus.html', context)


def references(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'category': category, }
    return render(request, 'references.html', context)


def contact(request):
    if request.method == 'POST':  # form post edildiyse
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
    current_user = request.user
    category = Category.objects.all()
    profile = UserProfile.objects.get(user_id=current_user.id)
    images = Images.objects.filter(transfer_id=id)
    transfer = Transfer.objects.get(pk=id)
    comments = Comment.objects.filter(transfer_id=id, status='True')
    context = {'category': category, 'transfer': transfer, 'images': images, 'comments': comments, 'profile': profile}
    return render(request, 'transfer_detail.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Invalid Login ")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {'category': category,
               }
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.jpg"
            data.save()
            messages.success(request, 'Welcome.... Your Profile was successfully registered')
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
               }
    return render(request, 'signup.html', context)


def sss(request):
    category = Category.objects.all()
    faq = FAQ.objects.all().order_by('ordernumber')
    context = {
        'category': category,
        'faq': faq
    }
    return render(request, 'faq_page.html', context)
