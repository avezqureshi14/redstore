import django
from django.forms import ModelForm
from .models import  Product, Topic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'



class CreteUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1']