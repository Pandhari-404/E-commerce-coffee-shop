from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime
from .models import Coffee, CartItem, Contact as ContactModel
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
# Create your views here.


def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})


def About(request):
    return render(request, 'about.html', {'coffee' : Coffee})

# def My_Cart(request):
#     return render(request, 'My Cart.html', {'coffee' : Coffee})


def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        # datetime.today()

        contact = ContactModel(name=name, phone=phone, email=email, address=address, date=datetime.today())
        contact.save()
    # Send email notification to admin

        subject = f"New Contact Message from {name}"
        message = f"""
            Name: {name}
            Phone: {phone}
            Email: {email}
            Address: {address}
            """
    
        send_mail(
            subject, 
            message, 
            'pandharipawde018@gmail.com', 
            ['pandharipawde018@gmail.com'], 
            fail_silently=False,
        )
        messages.success(request, " Yor message has been sent successfully!")
    return render(request, 'Contact.html', {'coffee' : Coffee})

# New Logic:

# 1
def add_to_cart(request, coffee_id):
    if request.method == 'POST':
    
        coffee = get_object_or_404(Coffee, id=coffee_id)

        cart_item, created = CartItem.objects.get_or_create(
            user = request.user,
            coffee=coffee,
        )
    

        if not created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1

        cart_item.save()
        messages.success(request, f"{coffee.name} added to cart")
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def My_Cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in items)

    return render(request, 'My Cart.html',{
        'items' : items,     
        'total' : total,
    })

# 3
def update_cart_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)

    if request.method == "POST":
        action = request.POST.get('action')
        if action == "increase":
            cart_item.quantity += 1
        elif action == "decrease" and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()

    return redirect('my cart')

# 4
def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    # messages.success(request, f"{cart_item.coffee.name} removed from cart")
    return redirect('my cart')  

# Message:

def order_success(request):
    order_id = 4
    email = request.user.email if request.user.is_authenticated else "user@gmail.com"

    return render(request, "order_success.html",{
        "order_id" : order_id,
        "email": email
    })

# 5
def checkout(request):
    return render(request, 'checkout.html')

# 6
def order_success(request):
    return render(request, 'order_success.html')

