from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
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

def delete_booking(request, booking_id):
    """
    view to delete selected booking
    """
    booking = get_object_or_404(MakeBooking, id = booking_id)
    booking.delete()
    messages.add_message(
        request, messages.SUCCESS,
        'Booking Deleted.'
    )
    return HttpResponseRedirect(reverse('page_view'))
        
