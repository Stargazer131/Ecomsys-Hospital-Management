from django.contrib import admin
from patients.models import Patient, MedicalRecord, LabTest, Prescription, Treatment

# Register your models here.
admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(LabTest)
admin.site.register(Prescription)
admin.site.register(Treatment)
