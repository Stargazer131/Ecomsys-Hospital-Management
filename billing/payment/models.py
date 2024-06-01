from django.db import models


class Invoice(models.Model):
    medical_record_id = models.BigIntegerField()
    date_issued = models.DateField()
    due_date = models.DateField()
    total_amount = models.FloatField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Invoice {self.pk} - Total: {self.total_amount}"


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.FloatField()
    status = models.CharField(max_length=50)
    method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment of {self.amount} for Invoice {self.invoice.pk} on {self.payment_date}"
