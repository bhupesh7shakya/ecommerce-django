# from decimal import Decimal
from decimal import Decimal
from rest_framework import serializers
from . import models
class CateogrySerializer(serializers.ModelSerializer):
    product_count=serializers.IntegerField(read_only=True)
    class Meta:
        model = models.Category
        fields=['title','product_count']
    
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Product
        fields=['id','name','inventory','category','price','price_with_tax']
        
    category=serializers.StringRelatedField()
    price_with_tax=serializers.SerializerMethodField('taxed_price')
    
    def taxed_price(self,product):
        return product.price+(product.price*Decimal(0.13))
    


class CartItemSerializer(serializers.ModelSerializer):
    product=serializers.StringRelatedField()
    # total_price=serializers.SerializerMethodField()
    class Meta:
        model=models.CartItem
        fields=[
            "cart",
            "product",
            "quantity",
            "price",
           
        ]
    
    
    # def get_total_price(self,cart_item:models.CartItem):
    #     return cart_item.quantity*cart_item.price
class CreateCartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.CartItem
        fields=[
            # "cart",
            "product",
            "quantity",
            "price",
        ]
    
class CartSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)

    # user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    cart_items=CartItemSerializer(many=True)
    # total=serializers.SerializerMethodField()
    class Meta:
        model=models.Cart
        fields=['id','user','cart_items',]
        

class CreateCartSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    # user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    cart_items=CreateCartItemSerializer(many=True)
    class Meta:
        model=models.Cart
        fields=['id','cart_items']
        
    def save(self, **kwargs):

        cart,_=models.Cart.objects\
            .get_or_create(user=self.context['request'].user)
      
        cart_items=self.validated_data['cart_items']
    
            
        cart_item_objects = [
            models.CartItem(
                quantity=item["quantity"],
                price=item["price"],
                product=item["product"],
                cart=cart
            )
            for item in cart_items
        ]


        models.CartItem.objects.bulk_create(cart_item_objects)


        