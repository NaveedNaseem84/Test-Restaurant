from django.shortcuts import render
from .models import models
from .forms import BookingForm

def page_view(request):

    if request.method == "POST":
        form = BookingForm(data=request.POST)
        if form.is_valid():
            form.save()          
    form = BookingForm()

    return render (
        request, 'book/book.html',
        {
            "form": form
        }
        )
    

