"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from directory import views as dir
from django.conf import settings
from django.conf.urls.static import static
from . import local_vars 

urlpatterns = [ 
    path('', dir.Homepage.as_view(), name = "home-page"),
    path('admin/', admin.site.urls, name = "admin"),

    path("dirs/", include('directory.urls', namespace='dirs')),
    path("books/", include('books.urls', namespace='books')),
    path("sales/", include('sales.urls', namespace='sales')),
    path("auth/", include('auth_user.urls', namespace='auth_user')),
    path("orders/", include('orders.urls', namespace='orders')),
    
] 

if local_vars.SERVER == 'local':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)