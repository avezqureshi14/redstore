from django.contrib import admin
from. models import Product, Topic
from. models import Customer
from. models import Order
from. models import OrderItem
from. models import ShippingAddress
from. models import Home


# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Home)
admin.site.register(Topic)
