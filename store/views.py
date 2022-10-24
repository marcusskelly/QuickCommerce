from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
# Create your views here.

def store(request):

	if request.user.is_authenticated:
		cliente = request.user.cliente
		pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
		items = pedido.productopedido_set.all()
		cartItems = pedido.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		pedido = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = pedido['get_cart_items']
		
	productos = Producto.objects.all()
	context = {'productos':productos, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)

def cart(request):

	if request.user.is_authenticated:
		cliente = request.user.cliente
		pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
		items = pedido.productopedido_set.all()
		cartItems = pedido.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		pedido = {'get_cart_total':0, 'get_cart_items':0}
		cartItems = pedido['get_cart_items']

	context = {'items':items, 'pedido':pedido,'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		cliente = request.user.cliente
		pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
		items = pedido.productopedido_set.all()
		cartItems = pedido.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		pedido = {'get_cart_total':0, 'get_cart_items':0}
		cartItems = pedido['get_cart_items']

	context = {'items':items, 'pedido':pedido,'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	
	data = json.loads(request.body)
	productoId = data['productoId']
	action = data['action']
	print('Action:', action)
	print('Producto:', productoId)

	cliente = request.user.cliente
	producto = Producto.objects.get(id=productoId)
	pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)

	productoPedido, created = ProductoPedido.objects.get_or_create(pedido=pedido, producto=producto)

	if action == 'add':
		productoPedido.cantidad = (productoPedido.cantidad + 1)
	elif action == 'remove':
		productoPedido.cantidad = (productoPedido.cantidad - 1)

	productoPedido.save()

	if productoPedido.cantidad <= 0:
		productoPedido.delete()
	

	return JsonResponse('Item was added', safe=False)
