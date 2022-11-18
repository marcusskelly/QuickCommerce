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
