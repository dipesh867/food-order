from django.shortcuts import render,redirect
from django.http import HttpResponse
from receipe.models import Food,Orders
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login")
def Receipe(request):
    queryset=Food.objects.order_by('name')

    if request.GET.get('search'):
       queryset= queryset.filter(name__icontains=request.GET.get('search'))

    context={'food':queryset}
    return render(request,"receipes.html",context)


@login_required(login_url="login")
def index(request):
    if request.method=='POST':
        data=request.POST
        food_price=data.get('price')
        food_name=data.get('name')
        food_description=data.get('description')
        food_image=request.FILES['image']
       
        Food.objects.create(
            name=food_name,
            description=food_description,
            image=food_image,
            price=food_price
            ) 
        messages.success(request,f"{food_name} created Successfully")
        return redirect('receipe')
    return render(request,"index.html")
    

def delete_food(request,id):
    queryset=Food.objects.get(id=id)
    queryset.delete()
    messages.success(request,f"{queryset.name} deleted Successfully")
    return redirect('receipe')


def update_food(request,id):
    queryset=Food.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        food_name=data.get('name')
        food_description=data.get('description')
        food_price=data.get('price')
        receipe_image=request.FILES.get('image')
        queryset.name=food_name
        queryset.description=food_description
        queryset.price=food_price
        if receipe_image:
            queryset.image=receipe_image
        queryset.save()
        messages.success(request,f'{queryset.name} updated Successfully')
        return redirect('receipe')
       
    context={'food':queryset}
    
    return render(request,"update.html",context)


def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            messages.info(request,"username not registered .please register")
            return redirect('login')
    
        user=authenticate(username=username,password=password)
        if user==None:
            messages.error(request,"invalid password")
            return redirect('login') 
        else:
            login(request,user)
            messages.success(request,f"Logged in as {username}")
            return redirect('receipe')
    return render(request,"login.html")


def register_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        name=request.POST.get("name")
        password=request.POST.get("password")

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"username already exists")
            return redirect('register')

        user=User.objects.create(
            username=username,
            first_name=name
        )
        user.set_password(password)
        user.save()
        return redirect('login')
    messages.info(request,"account created succesfully")
    return render(request,"register.html")
    
    
def logout_page(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect('login')


def food(request):
    queryset=Food.objects.order_by('name')
    if request.GET.get('search'):
       queryset= queryset.filter(name__icontains=request.GET.get('search'))

    context={'food':queryset}
    return render(request,"food.html",context)


def order_food(request,id):
    queryset=Food.objects.get(id=id)
    address = ''
    quantity = 1
    phone = ''
    if request.method=="POST":  
        data=request.POST
        address=data.get('address')
        quantity=data.get('quantity')
        phone=data.get('phone')
        order=queryset

        if len(str(phone))!= 10:
            messages.info(request,"phone number shoul be of 10 digits")
        else:
            Orders.objects.create(
                address=address,
                quantity=int(quantity),
                order=order,
                phone=phone,
                cost=int(order.price)*int(quantity)
                )
            messages.success(request,f'{order.name} is ordered Successfully')
            return redirect('myorder')
        
            
    return render(request,'order.html',context={'food':queryset,'address': address, 'quantity': quantity, 'phone': phone})
        
    
def myorder(request):
    queryset=Orders.objects.all()
    if request.GET.get('search'):
       queryset= queryset.filter(order__name__icontains=request.GET.get('search'))
       
    context={'food':queryset}
    return render(request,"myorder.html",context)


def cancel_order(request,id):
    queryset=Orders.objects.get(id=id)
    queryset.delete()
    messages.success(request,f"{queryset.order.name} is cancelled Successfully")
    return redirect('myorder')