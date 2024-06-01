from django.db import models
from general.models import Staff


class Doctor(models.Model):
    staff = models.OneToOneField(
        Staff, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Doctor {self.pk} - {self.staff.department}"


class Nurse(models.Model):
    staff = models.OneToOneField(
        Staff, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nurse {self.pk} - {self.staff.department}"


class Pharmacist(models.Model):
    staff = models.OneToOneField(
        Staff, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Pharmacist {self.pk} - {self.staff.department}"


class LabTechnician(models.Model):
    staff = models.OneToOneField(
        Staff, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50, unique=True)
    lab_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Lab Technician {self.pk} - {self.staff.department}"
