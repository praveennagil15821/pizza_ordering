from order.models import Pizza
from .serializers import PizzaSerializer
from rest_framework import viewsets

class PizzaViewset(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer