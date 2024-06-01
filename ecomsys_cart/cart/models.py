from django.db import models
import requests


# Create your models here.
class CartItem(models.Model):
    user_id = models.BigIntegerField()
    order_id = models.BigIntegerField(null=True, default=None, blank=True)
    product_id = models.BigIntegerField()
    
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(default=0.00)


    class Meta:
        db_table = 'cart_items'
        ordering = ['-date_added']


    def augment_quantity(self, quantity):
        self.quantity += int(quantity)
        self.save()
        
        
    def save(self, *args, **kwargs):
        url = f'http://localhost:8002/product/{self.product_id}/'
        response = requests.get(url)
        self.total_price = response.json()['price'] * self.quantity
        
        super().save(*args, **kwargs)

        