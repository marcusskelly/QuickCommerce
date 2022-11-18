from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from . utils import cookieCart

# Create your views here.

def store(request):

	if request.user.is_authenticated:
		cliente = request.user.cliente
		pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
		items = pedido.productopedido_set.all()
		cartItems = pedido.get_cart_items
	else:
		cookieData = cookieCart(request) # we can access whats in utils through request method
		cartItems = cookieData['cartItems']
		
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
		cookieData = cookieCart(request) # we can access whats in utils through request method
		cartItems = cookieData['cartItems']
		pedido = cookieData['pedido'] # This took me a while to realise it was wrong
		items = cookieData['items']

	context = {'items':items, 'pedido':pedido,'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		cliente = request.user.cliente
		pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
		items = pedido.productopedido_set.all()
		cartItems = pedido.get_cart_items
	else:
		cookieData = cookieCart(request) # we can access whats in utils through request method
		cartItems = cookieData['cartItems']
		pedido = cookieData['pedido']
		items = cookieData['items']

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

def processOrder(request):
	codigo_transaccion = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		cliente = request.user.cliente
		pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False) # inserts one record into table Pedido
		total = float(data['form']['total']) # We get the total value from the form in the fetch call 
		pedido.codigo_transaccion = codigo_transaccion

		if total == pedido.get_cart_total:
			pedido.completo = True
		pedido.save()

		# Si el pedido contiene productos no digitales, se crea un registro en tabla DireccionPedido
		if pedido.envio == True:
			DireccionPedido.objects.create(
			cliente=cliente,
			pedido=pedido,
			direccion=data['envio']['direccion'],
			ciudad=data['envio']['ciudad'],
			provincia=data['envio']['provincia'],
			codigo_postal=data['envio']['codigo_postal'],
			)
	else:
		print('User is not logged in')

	return JsonResponse('Payment submitted..', safe=False)