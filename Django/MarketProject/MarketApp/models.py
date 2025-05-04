from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=100)
    opening_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_time_from = models.TimeField()
    work_time_to = models.TimeField()

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    ssn = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

class Contact(models.Model):
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.EmailField()
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

class Product(models.Model):
    PRODUCT_TYPE = (
        ('food', 'food'),
        ('drinks', 'drinks'),
        ('bakery', 'bakery'),
        ('cosmetics', 'cosmetics'),
        ('hygiene', 'hygiene'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=PRODUCT_TYPE)
    local_product = models.BooleanField(default=False)
    code = models.CharField(max_length=100, unique=True)

class ProductInMarket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
