from django.db import models

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name
class Pizza(models.Model):
    def __str__(self):
        return self.name
    toppings = models.ManyToManyField(Topping)
    name = models.CharField(max_length = 200)
    price = models.IntegerField(default=0)
    SIZE_CHOICES = [
        ('S', "Small"),
        ('M',"Medium"),
        ('L',"Large"),
    ]
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='S')
 