from .models import MakeBooking
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = MakeBooking
        fields = ('name','email', 'phone', 'date', 'time_slot','number_of_people')
        widgets ={
            'date':forms.TextInput(attrs={'type':'date'}),
           
        }