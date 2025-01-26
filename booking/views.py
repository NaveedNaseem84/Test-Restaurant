#from django.shortcuts import render
#rom django.http import HttpResponse

# Create your views here.

#def booking_confirmation(request):
   # return HttpResponse("Hello, this is the bookings page.")

from django.shortcuts import render
#from django.contrib import messages
from .forms import BookingForm

# Create your views here.

def booking_view(request):
    """
    Renders the About page
    """
    if request.method == "POST":
        form = BookingFormForm(data=request.POST)
        if form.is_valid():
            form.save()
            #messages.add_message(request, messages.SUCCESS, "Booking request received!")    
    form = BookingForm()

    return render(
        request,
        "booking/booking.html",
        {
            #"booking": booking,
            "form": form
        },
    )