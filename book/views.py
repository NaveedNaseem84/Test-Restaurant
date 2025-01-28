from django.shortcuts import render
from .models import MakeBooking
from .forms import BookingForm


def page_view(request):


    if request.method == "POST":
        form = BookingForm(data=request.POST)
        if form.is_valid():
            form.save()          
    form = BookingForm()
    bookings = MakeBooking.objects.all() 

    return render (
        request, 'book/book.html',
        {
            "form": form,
            "bookings": bookings
        }
        )
def show_bookings(request):
    bookings = MakeBooking.objects.all()    
    return render (
        request, 'bookings.html',
        {
            "bookings": bookings
        }
    )

