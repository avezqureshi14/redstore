from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
import os
import datetime
from statistics import quantiles
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Home(models.Model):
    heading1 = models.CharField(max_length=200)
    description1 = models.CharField(max_length=180)
    heading2 = models.CharField(max_length=200)
    description2 = models.CharField(max_length=180)
    ReviewName = models.CharField(max_length=200)
    ReviewDescription = models.CharField(max_length=180)
    aboutUs = models.CharField(max_length=230)

    def __str__(self):
        return self.heading


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_image =  models.ImageField(null=
    True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Topic(models.Model):
    name = models.CharField(max_length=200, null=True, default="")
    def __str__(self):
        return self.name


class Product(models.Model):
    productid = models.AutoField
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=200)
    description = models.CharField(max_length=1000)
    delivery_days = models.CharField(max_length=200, null=True)
    topic =  models.ForeignKey(Topic, on_delete=models.SET_NULL, blank=True, null=True)
    digital = models.BooleanField(null=True, default=False, blank=False)
    image1 = models.ImageField(upload_to=filepath, default="")
    image2 = models.ImageField(upload_to=filepath, default="")
    image3 = models.ImageField(upload_to=filepath, default="")
    image4 = models.ImageField(upload_to=filepath, default="")
    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems =  self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems =  self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 



class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total =self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address

