from django.db import models


class Patient(models.Model):
    user_id = models.BigIntegerField()
    medical_history = models.TextField(null=True)
    allergies = models.TextField(null=True)

    def __str__(self):
        return f"Patient {self.pk}"


class MedicalRecord(models.Model):
    diagnosis = models.TextField()
    visit_date = models.DateField()
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Medical Record {self.pk}"


class LabTest(models.Model):
    test_name = models.CharField(max_length=100)
    test_date = models.DateField()
    result = models.TextField()
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.test_name} on {self.test_date}"


class Prescription(models.Model):
    medication_id = models.BigIntegerField()
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    prescribed_date = models.DateField()
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.medication_id} ({self.dosage}, {self.frequency})"


class Treatment(models.Model):
    description = models.TextField()
    type = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, null=True, blank=True)
