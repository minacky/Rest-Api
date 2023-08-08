from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # Add other fields as needed

class Category(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields as needed

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    is_delivered = models.BooleanField(default=False)
    # Add other fields as needed



class Reservation(models.Model):
   first_name = models.CharField(max_length=255)
   reservation_date=models.DateTimeField(auto_now_add=False)
   reservation_time=models.TimeField(default=dt.time(00, 00))

   def __str__(self):
      return self.first_name