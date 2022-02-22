from unicodedata import name
from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from .models import Customer

def customer_profile(sender, instance , create, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)