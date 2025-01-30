from django.shortcuts import render
from django.contrib import messages
from .models import MakeBooking
from .forms import BookingForm


def page_view(request):


    if request.method == "POST":
        form = BookingForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Booking created.'
    )          
    form = BookingForm(initial={'name':request.user})
    
    bookings = MakeBooking.objects.all()
    booking_count = bookings.filter(name = request.user).count()
    #bookings = MakeBooking.objects.filter(user=request.user) 

    return render (
        request, 'book/book.html',
        {
            "form": form,
            "bookings": bookings,
            "booking_count": booking_count
        }
        )
def show_bookings(request):
    bookings = MakeBooking.objects.all()    
    return render (
        request, 'book/bookings.html',
        {
            "bookings": bookings
        }
    )

