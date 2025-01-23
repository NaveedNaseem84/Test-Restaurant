from django.shortcuts import render
from django.views import generic
from .models import MenuItem

class MenuList(generic.ListView):
    queryset = MenuItem.objects.all()
    #template_name = "menuitem_list.html"
    template_name = "menu/menu.html"

