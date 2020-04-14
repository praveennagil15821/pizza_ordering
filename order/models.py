from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.core.validators import RegexValidator

# Create your models here.


class Toppings(models.Model):
    name=models.CharField(max_length=100,blank=True)
    price=models.IntegerField(null=True)
    desc=models.CharField(max_length=100,blank=True)
    
    
pizza_category = (
    ('Veg', 'Veg Pizza'),
    ('Non-Veg', 'Non-Veg Pizza'),
    ('Jain', 'Veg Pizza for Jains'),
)
class Pizza(models.Model):
    pizza_name=models.CharField(max_length=100,blank=False)
    pizza_description=models.CharField(max_length=200,blank=False)
    price=models.IntegerField(null=False) 
    pizza_image=models.ImageField(upload_to='pizza_pics',null=False)
    pizza_category=models.CharField(max_length=20,choices=pizza_category,blank=False)
    
    def __str__(self):
        return f'{self.id} {self.pizza_name[0:7]} {self.price}'


    
class Orders(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    pizza=models.ForeignKey(Pizza, on_delete=models.CASCADE)
    extra=models.ManyToManyField(Toppings,blank=True)   
    order_price=models.IntegerField(null=False)
    order_created=models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField(null=False,default=1)
    bill_name=models.CharField(max_length=100,blank=False)
    bill_mob=models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')],blank=False)
    bill_state=models.CharField(max_length=50,blank=False)
    bill_city=models.CharField(max_length=50,blank=False)
    bill_add=models.CharField(max_length=200,blank=False)
    updateable=models.IntegerField(null=False)

    
    def __str__(self):
        return f'{self.id} name= {self.pizza} date = {self.order_created}'

    def get_time_diff(self):
        if self.order_created:
            now = timezone.now()
            timediff = now - self.order_created
            timediff=int(timediff.total_seconds())
            if timediff <= self.updateable:
                return True
            else:
                return False
    def get_remaining_time(self):
        if self.order_created:
            now = timezone.now()
            timediff = now - self.order_created
            timediff=int(timediff.total_seconds())
            if timediff <= self.updateable:
                return int((self.updateable - timediff)/60)
                       

class Time_out(models.Model):    
    limit_minutes=models.IntegerField(null=False,default=10)

    def __str__(self):
        return f'Time out in minutes: {self.limit_minutes} minutes'
    
    