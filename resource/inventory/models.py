from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    contact_info = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100)
    price = models.FloatField()
    status = models.CharField(max_length=50, default='Intact')
    quantity = models.PositiveIntegerField()
    manufacturers = models.ManyToManyField(Manufacturer)

    def __str__(self):
        return self.name


class Bill(models.Model):
    pharmacist_id = models.BigIntegerField()
    import_date = models.DateField()
    total_price = models.FloatField()

    def __str__(self):
        return f"Bill id {self.pk}"


class Medication(models.Model):
    resource = models.OneToOneField(Resource, on_delete=models.CASCADE)
    expired_date = models.DateField()

    def __str__(self):
        return self.name


class Supply(models.Model):
    resource = models.OneToOneField(Resource, on_delete=models.CASCADE)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BillItem(models.Model):
    resource = models.OneToOneField(Resource, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
