"""python_34650 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from python_34650.views import hola_mundo
from products.views import create_product, list_products
from datos.views import create_contact, list_contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', hola_mundo),

    path('create_product/', create_product),
    path('list-products/', list_products),

    path('create_contact/', create_contact),
    path('list-contacts/', list_contacts),



]


