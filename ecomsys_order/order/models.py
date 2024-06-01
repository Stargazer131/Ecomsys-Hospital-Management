from django.db import models


# Create your models here.
class Order(models.Model):
    status_choices = [
        ('Canceled', 'Canceled'),
        ('Arrived', 'Arrived'),
        ('Transporting', 'Transporting'),
        ('Hold', 'Hold'),
    ]
    
    user_id = models.BigIntegerField() 
    status = models.CharField(max_length=30, choices=status_choices, default='Transporting')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()

    
    class Meta:
        db_table = 'orders'
        ordering = ['-created_timestamp']
        