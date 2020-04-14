from django import forms
from order.models import Orders
from django.forms import ModelForm

class OrderCreate(ModelForm):

    class Meta:
        model = Orders
        exclude = ('user','pizza','extra','order_price','order_created','quantity','updateable') 