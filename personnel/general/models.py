from django.db import models


class Staff(models.Model):
    user_id = models.BigIntegerField()
    hire_date = models.DateField()
    department = models.CharField(max_length=100)
    salary = models.BigIntegerField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"Staff {self.pk} - {self.department}"


class Manager(models.Model):
    staff = models.OneToOneField(
        Staff, on_delete=models.CASCADE)
    rank = models.CharField(max_length=100)

    def __str__(self):
        return f"Manager {self.pk} - {self.staff.department}"


class Receptionist(models.Model):
    staff = models.OneToOneField(
        Staff, on_delete=models.CASCADE)
    front_desk = models.CharField(max_length=100)

    def __str__(self):
        return f"Receptionist {self.pk} - {self.staff.department}"
