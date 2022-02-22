import imp
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [   
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('productpage/<str:pk>', views.productpage, name="productpage"),
    path('allproducts/', views.allproducts, name="allproducts"),
    path('createproduct/', views.createproduct, name="createproduct"),
    path('createcategory/', views.createcategory, name="createcategory"),
    path('updateproduct/<str:pk>', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<str:pk>',views.deleteproduct, name = 'deleteproduct'),
    path('user/', views.userPage, name="user"),
    path('slider/', views.slider, name="slider"),
    path('about/', views.about, name="about"),
    path('privacypolicy/', views.privacy, name="privacy"),
    path('DMCA/', views.dmca, name="dmca"),
    path('processOrder/', views.processOrder, name="processOrder"),
    path('contact/', views.contact, name="contact"),
    path('updateItem/', views.updateItem, name="updateItem"),


    
]
    