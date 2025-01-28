from django.db import models
from django.contrib.auth.models import User

TIME_SLOTS = [
    ("5.30","5.30"),
    ("6.30","6.30"),
    ("7.30","7.30"),
    ("8.30","8.30"),
    ("9.30","9.30"),
]

NO_OF_PEOPLE = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
]
# Create your models here.

class MakeBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateField()
    time_slot = models.CharField(choices=TIME_SLOTS)
    number_of_people = models.IntegerField(choices=NO_OF_PEOPLE)

    def __str__(self):
        return f"Booking for: {self.name} on {self.date} at {self.time_slot} for {self.number_of_people}"
