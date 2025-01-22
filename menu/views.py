from django.shortcuts import render
from django.views import generic
from .models import MenuItem
#from django.http import HttpResponse

# Create your views here.

#def menu(request):
    #return HttpResponse("Hello, this is the menu page.")

class MenuList(generic.ListView):
    queryset = MenuItem.objects.all()
    template_name = "menuitem_list.html"

