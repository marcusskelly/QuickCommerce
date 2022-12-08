import json
from . models import *

def cookieCart(request):

	#Create empty cart for now for non-logged in user
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}
		print('CART:', cart)

	items = []
	pedido = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
	cartItems = pedido['get_cart_items']

	for i in cart:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:
			cartItems += cart[i]['cantidad']

			producto = Producto.objects.get(id=i)
			total = (producto.precio * cart[i]['cantidad'])

			pedido['get_cart_total'] += total
			pedido['get_cart_items'] += cart[i]['cantidad']

			item = {
				'id':producto.id,
				'producto':{
					'id':producto.id,
					'nombre':producto.nombre, 
					'precio':producto.precio, 
				    'imagen':producto.imagen
					}, 
				'cantidad':cart[i]['cantidad'],
				'digital':producto.digital,
				'get_total':total
				}
			items.append(item)

			if producto.digital == False:
				pedido['shipping'] = True
		except:
			pass
			
	return {'cartItems':cartItems ,'pedido':pedido, 'items':items}

def cartData(request): # This function calls cookieCart() function which contains all items and their prices that have been added to the cart.
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
	return {'cartItems':cartItems ,'pedido':pedido, 'items':items}

def guestOrder(request,data):
	print('User is not logged in')

	print('COOKIES:', request.COOKIES)
	nombre = data['form']['nombre']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']
	cliente, created =Cliente.objects.get_or_create(email=email,)
	cliente.nombre = nombre
	cliente.save() # con estas lineas podemos guardar el email y el nombre de un cliente sin cuenta, y ver su historial de pedidos en la plataforma

	pedido = Pedido.objects.create(cliente=cliente,completo=False,) # Se crea un pedido

	for item in items:
		producto = Producto.objects.get(id=item['producto']['id'])

		productoPedido = ProductoPedido.objects.create(
			producto=producto,
			pedido=pedido,
			cantidad=(item['cantidad'] if item['quantity']>0 else -1*item['quantity']),
			) # With these lines we assign productos to productoPedido that eventually will be added to an order

	return cliente,pedido