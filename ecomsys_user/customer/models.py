from django.db import models


class Customer(models.Model):
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    
    account = models.OneToOneField('Account', on_delete=models.CASCADE)
    fullname = models.OneToOneField('Fullname', on_delete=models.CASCADE, blank=True, null=True)
    address = models.OneToOneField('Address', on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        db_table = 'customers'
        ordering = ['account__username']


    def __str__(self):
        return self.username


class Fullname(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    class Meta:
        db_table = 'fullnames'


    def __str__(self):
        return self.first_name


class Address(models.Model):
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=50)


    class Meta:
        db_table = 'address'


    def __str__(self):
        return self.city
    
    
class Account(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)


    class Meta:
        db_table = 'account'


    def __str__(self):
        return self.username
    
    