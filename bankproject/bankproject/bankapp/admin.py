from django.contrib import admin
from . models import District,Branch,Account,Materials,Customer


# Register your models here.
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Account)
admin.site.register(Materials)
admin.site.register(Customer)