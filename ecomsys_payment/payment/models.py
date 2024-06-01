from django.db import models


# Create your models here.
class Payment(models.Model):
    payment_choices = [
        ("Credit Card", "Credit Card"),
        ("Visa", "Visa"),
        ("Mastercard", "Mastercard"),
        ("Cash on Delivery", "Cash on Delivery"),
    ]
    
    status_choices = [
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("Failed", "Failed"),
        ("Refunded", "Refunded"),
        ("Canceled", "Canceled"),
        ("Partially Paid", "Partially Paid"),
        ("Expired", "Expired"),
    ]
    
    payment_choice_list = [pair[0] for pair in payment_choices]

    order_id = models.BigIntegerField(primary_key=True)
    method = models.CharField(max_length=30, choices=payment_choices)
    status = models.CharField(max_length=50, choices=status_choices, default='Pending')
    
    card_number = models.CharField(max_length=16, null=True, blank=True)
    expired_date = models.DateField(null=True, blank=True)
    security_code = models.CharField(max_length=6, null=True, blank=True)
    
    paid_amount = models.FloatField(default=0.00)
    debt_amount = models.FloatField(default=0.00)
    total_amount = models.FloatField(default=0.00)
    
    
    class Meta:
        db_table = "payments"
        
        
    def save(self, *args, **kwargs):
        self.debt_amount = max(self.total_amount - self.paid_amount, 0)
        super().save(*args, **kwargs)
