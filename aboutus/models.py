from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=100, unique=True)   
    description = models.TextField()   
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Info: {self.title}"


