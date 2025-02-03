from django.shortcuts import render
from django.contrib import messages
from .models import AboutUs
#from .forms import CollaborateForm
# Create your views here.

def about_me(request):
    """
    Renders the About page
    """  
    about = AboutUs.objects.all().first()
   
    count = AboutUs.objects.all().count()
    return render(
        request,
        "aboutus/about.html",
        {
            "about": about,
            "count": count,
           
        },
    )