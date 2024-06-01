from django.contrib import admin
from .models import Bill, BillItem, Manufacturer, Medication, Resource, Supply

# Register your models here.
admin.site.register(Bill)
admin.site.register(BillItem)
admin.site.register(Manufacturer)
admin.site.register(Medication)
admin.site.register(Resource)
admin.site.register(Supply)