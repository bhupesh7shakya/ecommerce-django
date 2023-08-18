from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.


class Category(models.Model):
    title=models.CharField(max_length=255,unique=True)
    
    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    BRONZE_MEMBER='B'
    GOLD_MEMBER='G'
    SILVER_MEMBER='S'
    
    MEMBERSHIP=[
        (BRONZE_MEMBER,'Bronze'),
        (GOLD_MEMBER,'Gold'),
        (SILVER_MEMBER,'Silver'),
    ]
   
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contact = models.IntegerField()
    membership=models.CharField(max_length=1,choices=MEMBERSHIP,default=BRONZE_MEMBER)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.firstname} ({self.contact})"

class Address(models.Model):
    customer = models.OneToOneField('Customer', on_delete=models.CASCADE,)
    street_name=models.CharField(max_length=100)
    tole_name=models.CharField(max_length=100)
    

class Order(models.Model):
    PENDING_STATUS='P'
    COMPLETED_STATUS='C'
    FAILED_STATUS='F'
    
    PAYMENT_STATUS=[
        (PENDING_STATUS,"Pending"),
        (COMPLETED_STATUS,'Completed'),
        (FAILED_STATUS,"Failed")
    ]
    place_at=models.DateTimeField(auto_now=True)
    payment_status=models.CharField(max_length=1,choices=PAYMENT_STATUS,default=PENDING_STATUS)
    user=models.ForeignKey(User,on_delete=models.PROTECT)

class OrderItem(models.Model):
    order=models.ForeignKey("Order",on_delete=models.PROTECT)
    product=models.ForeignKey("Product",on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    price=models.FloatField()



class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT,related_name="users_cart")

class CartItem(models.Model):
    cart=models.ForeignKey("Cart",on_delete=models.CASCADE,related_name="cart_items")
    product=models.ForeignKey("Product",on_delete=models.CASCADE,related_name="cart_products")
    quantity=models.PositiveSmallIntegerField()
    price=models.FloatField()
    