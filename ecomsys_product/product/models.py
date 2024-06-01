import random
from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=9.99)
    quantity = models.IntegerField(default=10)
    image = models.ImageField(upload_to='images/products/', null=True, blank=True)
    type = models.CharField(max_length=20, choices=[
        ('book', 'book'), ('clothes', 'clothes'), ('mobile', 'mobile')
    ])

    class Meta:
        db_table = 'products'
        ordering = ['name']


    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Product)
        super().save(*args, **kwargs)


def random_id(module):
    id_list = module.objects.values_list('id', flat=True)
    while True:
        id = random.randint(1, 1_000_000_000)
        if id not in id_list:
            break
    return id