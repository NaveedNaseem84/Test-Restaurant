from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MakeBooking
# Register your models here.

@admin.register(MakeBooking)
class MenuAdmin(admin.ModelAdmin):

    list_display = ('name', 'email','phone', 'date', 'time_slot', 'number_of_people')
    search_fields = ['name','email']
    list_filter = ('name','email')
   
