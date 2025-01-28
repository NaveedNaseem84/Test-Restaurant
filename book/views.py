from django.shortcuts import render
from django.views import generic
from .models import models

def page_view(request):
    return render (request, 'book/book.html')
    

