from django.db import models


class Appointment(models.Model):
    patient_id = models.BigIntegerField()
    doctor_id = models.BigIntegerField()
    appointment_datetime = models.DateTimeField()
    duration = models.CharField(max_length=30)
    note = models.TextField()
    location = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=30, default='Scheduled')
