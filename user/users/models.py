from django.db import models


class Fullname(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}".strip()


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}"


class Role(models.Model):
    role_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.role_name


class Account(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class User(models.Model):
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact_info = models.CharField(max_length=20)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    fullname = models.OneToOneField(Fullname, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"User: {self.account.username}"
