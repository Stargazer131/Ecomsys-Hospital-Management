from django.contrib import admin
from .models import Bed, Building, Furniture, MedicalEquipment, Room

# Register your models here.
admin.site.register(Bed)
admin.site.register(Building)
admin.site.register(Furniture)
admin.site.register(MedicalEquipment)
admin.site.register(Room)