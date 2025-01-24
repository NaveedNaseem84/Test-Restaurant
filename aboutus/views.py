from django.shortcuts import render
from django.views import generic
from .models import AboutUs
#from django.http import HttpResponse

# Create your views here.

#def menu(request):
    #return HttpResponse("Hello, this is the menu page.")

class About(generic.ListView):
    queryset = AboutUs.objects.all()
    #template_name = "aboutus.html"
    template_name = "aboutus/about.html"

