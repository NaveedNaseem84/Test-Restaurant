from django.db import models

TIME_SLOTS = [
    ("5.30","5.30"),
    ("6.30","6.30"),
    ("7.30","7.30"),
    ("8.30","8.30"),
    ("9.30","9.30"),
]

DAY = [
    ("Mon","Mon"),
    ("Tue","Tue"),
    ("Wed","Wed"),
    ("Thur","Thur"),
    ("Fri","Fri"),
    ("Sat","Sat"),
    ("Sun", "Sun"),
]

DATE = [
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
    ("11","11"),
    ("12","12"),
    ("13","13"),
    ("14","14"),
    ("15","15"),
    ("16","16"),

]

YEAR = [
    ("2025","2025"),
]

NO_OF_PEOPLE = [
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),


]

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    day = models.CharField(max_length=5, choices=DAY)
    date = models.DateField(max_length=2, choices=DATE)
    year = models.DateField(max_length=4, choices=YEAR) 
    number_of_people = models.IntegerField(choices=NO_OF_PEOPLE)

    def __str__(self):
        return f"Booking: {self.name} on:{self.day}/{self.date}/{self.year} for: {self.number_of_people}"   

