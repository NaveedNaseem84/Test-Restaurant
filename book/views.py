from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import MakeBooking
from .forms import BookingForm



def page_view(request):
    bookings = MakeBooking.objects.all()
    booking_count = bookings.filter(name=request.user).count()

    if request.method == "POST":         
        form = BookingForm(data=request.POST)
        if form.is_valid():
            currentbooking = form.save(commit=False)
            currentbooking.name = request.user
            form.save()            
            messages.add_message(request, messages.SUCCESS,'Booking created.')
            return HttpResponseRedirect(reverse('page_view'))                    

    form = BookingForm()
   
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
        

def update_booking(request, booking_id):
    bookings = get_object_or_404(MakeBooking, id=booking_id)

    if request.method == "POST":
        form = BookingForm(data=request.POST, instance=bookings)
        #form = BookingForm(initial={'name':bookings.name, 'phone':bookings.phone, 'date':bookings.datem } )
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Booking updated.')
            return HttpResponseRedirect(reverse('page_view'))
            
    form = BookingForm(instance=bookings)
             
    #form = BookingForm({
        #'name':bookings.name,
        #'email':bookings.email,
        #'phone':bookings.phone,
       # 'date':bookings.date,
       # 'time_slot': bookings.time_slot,
       # 'number_of_people':bookings.number_of_people
      #  } )
    
   
    
    #booking_count = bookings.filter(name = request.user).count()
    bookings = MakeBooking.objects.filter(user=request.user) 

    return render(
        request, 'book/update_booking.html',
        {
            "form": form,
            #"bookings": bookings,
            #"booking_count": booking_count
        }
        )
