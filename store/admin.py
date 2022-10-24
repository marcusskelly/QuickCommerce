from django.contrib import admin

from store.models import Cliente, DireccionPedido, Pedido, Producto, ProductoPedido

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(ProductoPedido)
admin.site.register(DireccionPedido)