from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Cliente(models.Model):
	usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return str(self.nombre) # Fix error when checking admin panel for cliente

class Producto(models.Model):
	nombre = models.CharField(max_length=200)
	precio = models.DecimalField(max_digits=7, decimal_places=2)
	digital = models.BooleanField(default=False,null=True, blank=True)
	imagen = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.nombre


	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Pedido(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
	dia_comprado = models.DateTimeField(auto_now_add=True)
	completo = models.BooleanField(default=False)
	codigo_transaccion = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def envio(self):
		envio = False
		productopedido = self.productopedido_set.all()
		for i in productopedido:
			if i.producto.digital == False:
				envio = True
		return envio

	@property
	def get_cart_total(self):
		productopedido = self.productopedido_set.all()
		total = sum([item.get_total for item in productopedido])
		return total 

	@property
	def get_cart_items(self):
		productopedido = self.productopedido_set.all()
		total = sum([item.cantidad for item in productopedido])
		return total 


class ProductoPedido(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
	pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True) # Si pongo clase Producto debajo de esta, no pilla la FK
	cantidad = models.IntegerField(default=0, null=True, blank=True)
	dia_añadido = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.producto.precio * self.cantidad
		return total

	

class DireccionPedido(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
	pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
	direccion = models.CharField(max_length=200, null=False)
	ciudad = models.CharField(max_length=200, null=False)
	provincia = models.CharField(max_length=200, null=False)
	codigo_postal = models.CharField(max_length=200, null=False)
	dia_realizado = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.direccion


