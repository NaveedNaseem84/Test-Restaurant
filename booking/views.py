from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def booking_confirmation(request):
    return HttpResponse("Hello, this is the bookings page.")