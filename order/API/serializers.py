from rest_framework import serializers
from order.models import Pizza

class PizzaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pizza
        fields = ['pizza_name','pizza_description', 'price', 'pizza_image']
