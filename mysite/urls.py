"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog
from home import views
from reservations import views as reservationsviews

urlpatterns = [
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('transfer/', include('transfer.urls')),
    path('user/', include('user.urls')),
    path('reservations/', include('reservations.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('references/', views.references, name='references'),
    path('contact/', views.contact, name='contact'),
    path('category/<int:id>/<slug:slug>/', views.category_transfer, name='category_transfer'),
    path('transfer/<int:id>/<slug:slug>/', views.transfer_detail, name='transfer_detail'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('reservcart/', reservationsviews.reservcart, name='sss'),
    path('signup/', views.signup_view, name='signup_view'),
    path('sss/', views.sss, name='sss'),

]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
