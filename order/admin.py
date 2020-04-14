from django.contrib import admin
from . models import *

# Register your models here.
class ToppingsAdmin(admin.ModelAdmin):
    list_display=('name','price')
    search_fields=('name','price')

class PizzaAdmin(admin.ModelAdmin):
    list_display=('pizza_name','price','pizza_category')
    search_fields=('name','price','pizza_category')

class OrdersAdmin(admin.ModelAdmin):
    list_display=('id','user','bill_name','pizza','order_price','quantity','bill_mob')
    search_fields=('id','user','bill_name','price',)

# Register your models here.
admin.site.register(Toppings,ToppingsAdmin)
admin.site.register(Pizza,PizzaAdmin)
admin.site.register(Orders,OrdersAdmin)
admin.site.register(Time_out)