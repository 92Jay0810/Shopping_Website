from ninja import Schema, NinjaAPI
from ninja.orm import create_schema
from typing import List
from shop.models import Products, Cart, CartItem
from django.shortcuts import get_object_or_404
api = NinjaAPI()


class ProductsIn(Schema):
    id: int
    title: str
    price: float
    discount_price: float
    category: str
    description: str
    image: str


class CartIn(Schema):
    id: int
    user_id: int
    complete: bool


class ProductsOut(Schema):
    id: int
    title: str
    price: float
    discount_price: float
    category: str
    description: str
    image: str


class CartOut(Schema):
    id: int
    user_id: int
    complete: bool


class CartItemOut(Schema):
    product_id: int
    cart_id: int
    quantity: int


@api.get("/products", response=List[ProductsOut])
def list_products(request):
    products = Products.objects.all()
    return products


@api.get("/product/{product_id}", response=ProductsOut)
def get_product(request, product_id: int):
    product = get_object_or_404(Products, id=product_id)
    return product


@api.post("/product")
def create_product(request, payload: ProductsIn):
    product = Products.objects.create(**payload.dict())
    return {"id": product.id}


@api.put("/product/{product_id}")
def update_product(request, product_id: int, payload: ProductsIn):
    product = get_object_or_404(Products, id=product_id)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()
    return {"success": True}


@api.delete("/product/{product_id}")
def delete_product(request, product_id: int):
    product = get_object_or_404(Products, id=product_id)
    product.delete()
    return {"success": True}


@api.get("/carts", response=List[CartOut])
def list_carts(request):
    carts = Cart.objects.all()
    return carts


@api.get("/cart/{cart_id}", response=CartOut)
def get_cart(request, cart_id: int):
    cart = get_object_or_404(Cart, id=cart_id)
    return cart


@api.post("/cart")
def create_cart(request, payload: CartIn):
    cart = Cart.objects.create(**payload.dict())
    return {"id": cart.id}


@api.put("/cart/{cart_id}")
def update_cart(request, cart_id: int, payload: CartIn):
    cart = get_object_or_404(Cart, id=cart_id)
    for attr, value in payload.dict().items():
        setattr(cart, attr, value)
    cart.save()
    return {"success": True}


@api.delete("/cart/{cart_id}")
def delete_cart(request, cart_id: int):
    cart = get_object_or_404(Cart, id=cart_id)
    cart.delete()
    return {"success": True}


@api.get("/cartitems", response=List[CartItemOut])
def list_cartitems(request):
    cartitems = CartItem.objects.all()
    return cartitems


@api.get("/cartitem_quantity", response=CartItemOut)
def get_cartitem(request, product_id: int, cart_id: int):
    cartitem = get_object_or_404(CartItem, product=product_id, cart=cart_id)
    return cartitem


@api.put("/cartitem_quantity")
def update_cartitems(request, product_id: int, cart_id: int,  quantity: int):
    cartitems = get_object_or_404(CartItem, product=product_id, cart=cart_id)
    setattr(cartitems, "quantity", quantity)
    cartitems.save()
    return {"success": True}


@api.delete("/cartitem")
def delete_cartitems(request, product_id: int, cart_id: int):
    cartitem = get_object_or_404(CartItem, product=product_id, cart=cart_id)
    cartitem.delete()
    return {"success": True}
