from django.contrib import admin
from healthcare.models import Doctor, LabTechnician, Nurse, Pharmacist

# Register your models here.
admin.site.register(Doctor)
admin.site.register(LabTechnician)
admin.site.register(Nurse)
admin.site.register(Pharmacist)
