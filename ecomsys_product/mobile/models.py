from django.db import models
from product.models import random_id, Product
from clothes.models import Manufacturer


# Create your models here.
class MobileType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    
    class Meta:
        db_table = 'mobile_types'
        ordering = ['name']


    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(MobileType)
        super().save(*args, **kwargs)


class Mobile(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='mobiles')
    mobile_type = models.ForeignKey('MobileType', on_delete=models.CASCADE, related_name='mobiles')
    rom_size = models.IntegerField(default=64000) # in MB
    ram_size = models.IntegerField(default=6000)
    display_resolution = models.CharField(max_length=50, default='720 x 1080')
    chip = models.CharField(max_length=50, default='Standard chip')


    class Meta:
        db_table = 'mobiles'
        ordering = ['product__name']


    def __str__(self):
        return self.product.name
