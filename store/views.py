from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
import json
import datetime
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import * 
from . utils import cookieCart, cartData, guestOrder
from .filters import OrderFilter
from .forms import OrderForm,CreateUserForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm,OrderForm

from .decorators import unathenticated_user,allowed_users, admin_only

# Create your views here.


@unathenticated_user
def registerPage(request):
	
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				cliente = request.user.cliente
				"""  
				username = form.cleaned_data.get('username')
				group = Group.objects.get(name='customer')
				user.groups.add(group)
				"""
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')

		context = {'form':form}
		return render(request, 'store/register.html',context)

@unathenticated_user
def loginPage(request):
 	
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				cliente = request.user.cliente
				return redirect('store')
			else:
				messages.info(request, 'Username or password is incorrect')
				
		context = {}
		return render(request, 'store/login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def store(request):

	data = cartData(request) # we can access whats in utils through request method. 
	cartItems = data['cartItems']
	productos = Producto.objects.all()

	myFilter = OrderFilter(request.GET,queryset=productos)

	productos = myFilter.qs	
	
	context = {'productos':productos, 'cartItems':cartItems,'myFilter':myFilter}
	return render(request, 'store/store.html', context)

@login_required(login_url='login')
@admin_only
def dashBoard(request):
	orders = Pedido.objects.all()
	customers = Cliente.objects.all()

	total_customers = customers.count()

	total_orders = Pedido.objects.all().count()



	context = {'customers':customers, 'orders':orders,
	'total_customers':total_customers,'total_orders':total_orders}
	return render(request, 'store/dashboard.html', context)

def customer(request,pk):
	
	cliente = Cliente.objects.get(id=pk)
	data = cartData(request)
	items = data['items'] # try to access products that have been registered for that order and print them in the interface
	pedido= cliente.pedido_set.all()
	
	total_orders = pedido.count()


	context={'cliente':cliente, 'pedido':pedido, 'total_orders':total_orders,'items':items}
	return render(request, 'store/customer.html',context)

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