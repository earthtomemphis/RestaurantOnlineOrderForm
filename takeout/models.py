from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    dish_name = models.CharField(max_length=255)
    dish_image = models.ImageField(upload_to='img/', null=True, blank=True)
    dish_price = models.DecimalField(max_digits=4, decimal_places=2)
    dish_calories = models.IntegerField()

    def __str__(self):
        return str(self.dish_name)



class Order(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=30, null=True)
    delivery = 'Delivery'
    takeout = 'Takeout'
    DELIVERY_PICKUP_CHOICE = [
        (delivery, 'Delivery'),
        (takeout, 'Takeout'),
    ]
    delivery_pickup = models.CharField(max_length=8, choices=DELIVERY_PICKUP_CHOICE, default=takeout)
    address_line1 = models.CharField(max_length=30, null=True)
    address_line2 = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    zipcode = models.IntegerField(null=True)
    menu_item1 = models.CharField(max_length=30, null=True)
    menu_item2 = models.CharField(max_length=30, null=True)
    menu_item3 = models.CharField(max_length=30, null=True)
    payment_method = models.CharField(max_length=255, null=True)
    password1 = models.CharField(max_length=255, null=True)
    password2 = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.user)

    def delivery_pickup_choice(self):
        return self.delivery_pickup in {self.delivery, self.pickup} 