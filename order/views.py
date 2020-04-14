from django.shortcuts import render, redirect, get_object_or_404
from order.models import Pizza, Toppings, Orders, Time_out
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from order.forms import OrderCreate
import datetime
# Create your views here.


def calculate_edit_time():
    t2 = Time_out.objects.first()
    t2 = t2.limit_minutes * 60
    diff = t2
    return (int(diff))

def recent_orders(request):
    if request.user.is_authenticated:        
        x=[x for x in Orders.objects.filter(user=request.user) if x.get_time_diff()]
        
        if len(x) < 5:
            x=Orders.objects.filter(user=request.user).order_by('-order_created')[:5]
        return x
    else:
        return None    
@login_required
def OrdersListView(request):    
    context={
        'heading': 'Orders',
        'allorders':1,
        'orders':Orders.objects.filter(user=request.user).order_by('-order_created')
    }
    return render(request,'order/bookings.html',context)   

def home(request):
    if request.method == "POST":
        # print(request.POST.getlist('toppings_val'))
        request.session['pizza_id'] = request.POST.get("pizza_no")
        request.session['toppings'] = request.POST.getlist('toppings_val')
        if request.POST.get('qty'):
            request.session['quantity'] = request.POST.get('qty')
        else:
            request.session['quantity'] = 1
        return redirect('pizza_booking')

    heading = "Menu"
    
    content = {
        'pizzas': Pizza.objects.all(),
        'toppings': Toppings.objects.all(),
        'heading': heading,
        'orders1': recent_orders(request),

    }

    return render(request, 'order/home.html', content)


def pizza_booking(request):

    if request.session.get('pizza_id'):
        pizza_id = request.session.get('pizza_id')
        try:
            toppings = request.session.get('toppings')
            quantity = request.session.get('quantity')
            pizza = Pizza.objects.get(pk=pizza_id)
        except:
            return redirect('home')

        heading = "Checkout"
        total = pizza.price
        toppping_objects = []
        try:
            for top in toppings:
                if top:
                    topping = Toppings.objects.get(name=top)
                    toppping_objects.append(topping.id)
                    #print('total ',total,' + ',topping.price,'=',end='')
                    total += topping.price
                    # print(total)
                else:
                    break

        except:
            return redirect('home')
        total = total * int(quantity)

        if request.method == "POST":
            if request.user.is_authenticated:
                form = OrderCreate(request.POST)
                print('got')
                if form.is_valid():
                    order = form.save(commit=False)
                    order.pizza, order.user = pizza, request.user

                    order.order_price, order.quantity = total, quantity
                    order.updateable = calculate_edit_time()
                    print(order.updateable)
                    order.save()
                    for top in toppping_objects:
                        order.extra.add(top)

                    order.save()
                    messages.success(
                        request, f'{request.user} your order has been placed!')
                    return redirect('home')

                else:
                    messages.success(request, f'Please enter valid details!')

        form = OrderCreate()
        content = {
            'heading': heading,
            'update':'True',
            'toppings': toppings,
            'quantity': quantity,
            'pizza': pizza,
            'total': total,
            'orders1': recent_orders(request),
            'form': form
        }

        return render(request, 'order/order.html', content)

       # print('total sum of money =',total)
        # print(request.session.get('quantity'))

    else:
        raise Http404


def order_update(request, id):
    pk = id
    if request.user.is_authenticated:
        try:
            order = Orders.objects.get(pk=pk)
            if request.user.id == order.user.id:
                if order.get_time_diff() == False:
                    messages.success(
                        request, f'Order update session timed out!')
                    return redirect('home')

                if request.method == "POST":
                    order.extra.clear()
                    if int(request.POST.get('qty')):
                        order.quantity = request.POST.get('qty')
                    toppings = request.POST.getlist('top1')
                    for i in toppings:
                        topping = Toppings.objects.get(id=i)
                        order.extra.add(topping.id)

                    order.save()
                    request.session['order_id'] = order.id
                    print('saved successfully')

                    return redirect('order_delivery_update')

                content = {
                    'orders1': recent_orders(request),
                    'heading': 'Order Update',
                    'toppings': Toppings.objects.all(),
                    'selected_toppings': list(order.extra.all()),
                    'order': order,
                }
                return render(request, 'order/order_update.html', content)

            else:
                raise Http404
        except:
            raise Http404
    else:
        raise Http404

def order_delivery_update(request):
    pk=request.session.get('order_id')
    if request.user.is_authenticated:
        try:
            order = Orders.objects.get(pk=pk)
            if request.user.id == order.user.id:
                if order.get_time_diff() == False:
                    messages.success(
                        request, f'Your order update session timed out!')
                    return redirect('home')
                total = order.pizza.price
                
                for topping in order.extra.all():                    
                    total += topping.price

                total = total * int(order.quantity)
                order.order_price=total
                order.save()
                if request.method == "POST":
                    form = OrderCreate(request.POST,instance=order)
                    
                    if form.is_valid(): 
                    
                        form.save()                       
                        messages.success(
                            request, f'Hi {request.user}! your order has been updated.')
                        return redirect('home')

                
                    
                
                content = {
                    'heading': 'Billing Update',
                    'update':1,
                    'order': order,
                    'pizza': order.pizza,
                    'toppings': order.extra.all(),
                    'total': total,
                    'orders1': recent_orders(request),
                
                }
                return render(request, 'order/order.html', content)

            else:
                raise Http404
        except:
            raise Http404
    else:
        raise Http404
