from django.shortcuts import render
from django.views import generic
from .models import WelcomeInfo

class WelcomeList(generic.ListView):
    queryset = WelcomeInfo.objects.all()
    #template_name = "welcomeinfo_list.html"
    template_name = "welcome/index.html"

#from django.http import HttpResponse

# Create your views here.

#def index(request):
 #   return HttpResponse("Hello, this is the welcome page.")