from os import name
from .function import *
from django.http.response import Http404
from restaurant_sys.models import dish, restaurant
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .views import *
# Create your views here.
BACKGROUND_URL="https://scontent.xx.fbcdn.net/v/t1.15752-9/p160x160/256270882_925591381423228_4864508612004631979_n.jpg?_nc_cat=103&ccb=1-5&_nc_sid=aee45a&_nc_ohc=Y1XadNSEnYgAX-WrOYk&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=1f41dce50beb30bfc8b25cfb7c13b0cb&oe=61B584D5"

def hello(request):
    return render(request,"index.html")

def restaurant_view(request,restname):
    try:
        r= restaurant.objects.get(name=restname)
        print(r.name)
        food=r.dishes.filter(type='Food')
        drink=r.dishes.filter(type='Drink')
        return render(request,"index.html",{'r':r,'f':food,'d':drink,'back_url':BACKGROUND_URL})
    except:
        return Http404

def buy_site(request,restname):
    if request.method=="POST":
        try:
            r= restaurant.objects.get(name=restname)
            d_l=request.POST['input'].split(",")
            dsh=[dish.objects.get(name=x) for x in d_l]
            print(dsh)
            return render(request,"order.html",{'r':r,'dishes':dsh,'back_url':BACKGROUND_URL})
        except:
            pass

def order_handle(request,restname):
    if request.method=="POST":
        dict=request.POST
        print(request.POST['restname'])
        r=restaurant.objects.get(name=request.POST['restname'])
        create_bill(dict)
        print(dict.keys())
    return render(request,"thankyou.html",{'r':r,'back_url':BACKGROUND_URL})

def loginPage(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/manage_order')
            print("OK")
        else:
            messages.info(request,"Wrong username or pasword")

        pass
    return render(request,"login.html",{'back_url':BACKGROUND_URL})

def logoutUser(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def manage_order(request):
    o=[x for x in bill_order.objects.all()]
    o.reverse()
    return render(request,"manage_order.html",{'o':o,'back_url':BACKGROUND_URL})

@login_required(login_url='/login')
def manage_order_detail(request,order_id):
    b=bill_order.objects.get(id=order_id)
    if request.method=="POST":
        b.finish= not b.finish
        b.save()
        return redirect('/manage_order')
    b_i=b.bill_item.all()
    b_i=[{
        'name':x.item_name.name,
        'price_each':float(x.item_name.price),
        'price': float(x.amount*x.item_name.price),
        'amount':x.amount,
    } for x in b_i ]
    print(b_i)
    return render(request,"manage_order_detail.html",{'b':b,'b_i':b_i,'back_url':BACKGROUND_URL})
