from django.db import models
from django.contrib.auth.models import User

VALID_CHOICES = [
    ("Yes", "Yes"),
    ("No", "No"),      
    ]


# Create your models here.
class WelcomeInfo(models.Model):
    promotion_title = models.CharField(max_length=150, default="null")    
    description = models.TextField(blank = True)
    #contact_info = models.TextField()
    is_valid = models.CharField(max_length=15, choices=VALID_CHOICES, blank=False)    
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Main Heading: {self.promotion_title}"