from django.shortcuts import render, redirect, reverse
from .models import Products, Cart, CartItem
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from django.contrib.auth.forms import UserCreationForm


def index(request):
    product_all = Products.objects.all()

    # code for search
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_all = product_all.filter(title__icontains=item_name)

    # code for pagitator
    paginator = Paginator(product_all, 4)
    page = request.GET.get('page')
    product_all = paginator.get_page(page)

    cart = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(
            user=request.user, complete=False)

    return render(request, 'shop/index.html', {
        'product_all': product_all,
        'cart': cart,
    })


def detail(request, id):
    product_object = Products.objects.get(id=id)
    cart = None
    cartitem = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(
            user=request.user, complete=False)
        cartitem = cart.cartitems.all()
    return render(request, 'shop/detail.html', {
        'product_object':  product_object,
        "cart": cart,
    })


def cart(request):
    cart = None
    cartitem = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(
            user=request.user, complete=False)
        cartitem = cart.cartitems.all()
    return render(request, 'shop/cart.html', {
        "cart": cart,
        "cartitems": cartitem,
    })


def addToCart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Products.objects.get(id=product_id)
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(
            user=request.user, complete=False)
        cartitem, created_item = CartItem.objects.get_or_create(
            cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()
        number_of_item = cart.total_number
    return JsonResponse(number_of_item, safe=False)


def decreaseCart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Products.objects.get(id=product_id)
    number_of_item = 0
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user, complete=False)
        cartitem = CartItem.objects.get(cart=cart, product=product)
        if cartitem.quantity > 1:
            cartitem.quantity -= 1
            cartitem.save()
        elif cartitem.quantity == 1:
            cartitem.delete()
        number_of_item = cart.total_number
    return JsonResponse(number_of_item, safe=False)


def deleteCartitem(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Products.objects.get(id=product_id)
    number_of_item = 0
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user, complete=False)
        cartitem = CartItem.objects.get(cart=cart, product=product)
        cartitem.delete()
        number_of_item = cart.total_number
    return JsonResponse(number_of_item, safe=False)


def checkout(request):
    cart = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(
            user=request.user, complete=False)
    cart.complete = True
    cart.save()
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {
        "form": form,
    })
