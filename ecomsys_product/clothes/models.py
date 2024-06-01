from django.db import models
from product.models import random_id, Product


# Create your models here.
class Manufacturer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True) 


    class Meta:
        db_table = 'manufacturers'
        ordering = ['name']
    
    
    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Manufacturer)
        super().save(*args, **kwargs)
        


class Style(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)


    class Meta:
        db_table = 'styles'
        ordering = ['name']


    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Style)
        super().save(*args, **kwargs)
        
        
class ClothingItemStyle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    clothingitem = models.ForeignKey('ClothingItem', on_delete=models.CASCADE)
    style = models.ForeignKey('Style', on_delete=models.CASCADE)
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(ClothingItemStyle)
        super().save(*args, **kwargs)
        
        
    class Meta:
        db_table = 'clothes_styles'


class ClothingItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    styles = models.ManyToManyField('Style', through='ClothingItemStyle')
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, related_name='clothing_items')


    class Meta:
        db_table = 'clothes'
        ordering = ['product__name']


    def __str__(self):
        return self.product.name

