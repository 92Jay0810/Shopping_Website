from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum(item.price for item in cartitems)
        return total

    @property
    def total_number(self):
        cartitems = self.cartitems.all()
        quantity = sum(item.quantity for item in cartitems)
        return quantity


class CartItem(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="items")
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        new_price = self.product.price*self.quantity
        return new_price
