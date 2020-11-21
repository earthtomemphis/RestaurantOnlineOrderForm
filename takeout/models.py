from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    address_line1 = models.CharField(max_length=255, null=True)
    address_line2 = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    zipcode = models.IntegerField(null=True)
    menu_item1 = models.CharField(max_length=255, null=True)
    menu_item2 = models.CharField(max_length=255, null=True)
    menu_item3 = models.CharField(max_length=255, null=True)
    delivery_pickup = models.CharField(max_length=255, null=True)
    payment_method = models.CharField(max_length=255, null=True)
    password1 = models.CharField(max_length=255, null=True)
    password2 = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.user)