from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name = "store"),
    path('cart', views.cart, name = "cart"),
    path('checkout', views.checkout, name = "checkout"),
    path('register', views.registerPage, name = "register"),
    path('login', views.loginPage, name = "login"),
    path('logout', views.logoutUser, name = "logout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('customer/<int:pk>', views.customer, name="customer"),
    path('dashboard', views.dashBoard, name="dashboard"),
]