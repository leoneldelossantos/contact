from django.shortcuts import render
from django.http import  HttpResponse


# Create your views here.

from datos.models import Datos

def create_contact(request):
    new_contact = Datos.objects.create(name='Marcela Schenone', number=42472038, bool=True)
    print(new_contact)
    new_contact_1 = Datos.objects.create(name='Jorge Schenone', number=47952844, bool=True)
    print(new_contact_1)
    new_contact_2 = Datos.objects.create(name='Alfredo Schenone', number=42417650, bool=True)
    print(new_contact_2)
    return HttpResponse(' Se creo los 3 nuevos contactos')

def list_contacts(request):
    all_contacts = Datos.objects.all()
    print (all_contacts)
    context = {
        'datos': all_contacts,
    }
    return render (request, 'list_contacts.html' , context=context)