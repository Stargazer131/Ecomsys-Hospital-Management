from django.contrib import admin
from users.models import Fullname, Address, Role, Account, User

# Register your models here.
admin.site.register(Fullname)
admin.site.register(Address)
admin.site.register(Role)
admin.site.register(Account)
admin.site.register(User)
