from math import ceil, prod
import os
from django.db.models import Q
from email.headerregistry import Group
from unicodedata import name
from django.contrib.auth.decorators import login_required
from itertools import product
import json
from django.http import JsonResponse
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from eapp.decorators import allowed_users, unauthenticated_user
from .form import CreteUserForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django.template import context
from .form import ProductForm, TopicForm
from django.shortcuts import redirect, render
from.models import*

# Create your views here.


@unauthenticated_user
def registerPage(request):

    form = CreteUserForm()
    if request.method == 'POST':
        form = CreteUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)   
            Customer.objects.create(
                user=user,
                name=user.username,
            )
            messages.success(request, username + " account was created")
            return redirect('login')
    context = {"form": form}
    return render(request, 'register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')


# def home(request):

#     context = {}

#     return render(request, 'home.html', context)

def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']   
    context = {"cartItems":cartItems}
    return render(request, 'home.html', context)    


def navbar(request):
  if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
  else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']   
        context = {"cartItems":cartItems}
        return render(request, 'navbar.html', context)


def allproducts(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    # make only one context for fetching products and search
    topics = Topic.objects.all()
    products = Product.objects.filter(
        Q(topic__name__icontains=q)
    )

    context = {"products": products, "topics": topics, "cartItems":cartItems}
    return render(request, 'allproducts.html', context)


@login_required(login_url='login')
def createproduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('allproducts')
    context = {"form": form}

    return render(request, 'createproduct.html', context)


def createcategory(request):
    form = TopicForm()
    context = {'form': form}
    if request.method == 'POST':
        form = TopicForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('createproduct')
    return render(request, 'createcategory.html', context)


def updateproduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(product.image) > 0:
                os.remove(product.image.path)
            product.image = request.FILES['image']
            product.name = request.POST.get('name')
            product.price = request.POST.get('price')
            product.description = request.POST.get('description')
            product.delivery_days = request.POST.get('delivery_days')
            product.save()
            return redirect('allproducts')

    context = {"product": product}
    return render(request, 'updateproduct.html', context)


def deleteproduct(request, pk):
    prouctContainer = Product.objects.get(id=pk)
    if request.method == 'POST':
        prouctContainer.delete()
        return redirect('allproducts')

    context = {'prouctContainer': prouctContainer}
    return render(request, 'deleteproduct.html', context)


def productpage(request, pk):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']      
    product = Product.objects.get(id=pk)
    products = Product.objects.all()

    context = {'product': product,"cartItems":cartItems,'products': products}

    return render(request, 'productpage.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']  
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
    context = {"items":items, "order":order,"cartItems":cartItems}
    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items'] 
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
    context = {"items":items, "order":order,"cartItems":cartItems}
    return render(request, 'checkout.html', context)


def userPage(request):

    context = {}
    return render(request, 'user.html', context)


def about(request):

    context = {}

    return render(request, 'about.html', context)


def contact(request):

    context = {}

    return render(request, 'contact.html', context)


def privacy(request):

    context = {}

    return render(request, 'privacy.html', context)


def dmca(request):

    context = {}

    return render(request, 'dmca.html', context)


def slider(request):
    products = Product.objects.all()

    context = {"products":products}
    return render(request, 'slider.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('action:',action)
    print('productId:',productId) 

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                state=data['shipping']['state'],
                city=data['shipping']['city'],
                zipcode=data['shipping']['zipcode'],

            )        

    return JsonResponse('Payment submitted...', safe=False) 