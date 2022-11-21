from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from . utils import cookieCart, cartData, guestOrder

# Create your views here.

def store(request):

	data = cartData(request) # we can access whats in utils through request method. 
	cartItems = data['cartItems']
		
	productos = Producto.objects.all()
	context = {'productos':productos, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)

def cart(request):

	data = cartData(request) # we can access whats in utils through request method. 
	cartItems = data['cartItems']
	pedido = data['pedido'] # This took me a while to realise it was wrong
	items = data['items']

	context = {'items':items, 'pedido':pedido,'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	
	data = cartData(request) # we can access whats in utils through request method
	cartItems = data['cartItems']
	pedido = data['pedido']
	items = data['items']

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

def processOrder(request): # This method will create an order regardless of the type of user and will store it in database
	codigo_transaccion = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		cliente = request.user.cliente
		pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=True) # inserts one record into table Pedido
		
	else:
		
		cliente, pedido = guestOrder(request,data) # adds value to these two variables (cliente, pedido) from function guestOrder()

		total = float(data['form']['total']) # We get the total value from the form in the fetch call 
		pedido.codigo_transaccion = codigo_transaccion

		if total == pedido.get_cart_total:
			pedido.completo = True
		pedido.save() # With these lines we make sure that an order is created regardless of the condition of being a guest user or registered

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

	return JsonResponse('Payment submitted..', safe=False)