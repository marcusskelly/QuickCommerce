import django_filters

from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Producto
        fields = '__all__'
        exclude = ['imagen','nombre']