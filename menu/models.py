from django.db import models
from django.contrib.auth.models import User

CATEGORIES_CHOICES = [
    ("Starter", "Starter"),    
    ("Side", "Side"),
    ("Dessert", "Dessert"),
    ("Mains", "Mains"),
    ("Drink", "Drink"),    
    ]


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=15, choices=CATEGORIES_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Menu item: {self.name} Category: {self.category} Price: {self.price}"


