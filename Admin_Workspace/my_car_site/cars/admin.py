from dataclasses import fields
import imp
from django.contrib import admin
from cars.models import Car
# Register your models here.



# admin.site.register(Car)



# Customising the administration form 
class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('TIME INFORMATION', {'fields' : ['year']}),
        ('CAR INFORMATION', {'fields': ['brand']})
    ]
admin.site.register(Car, CarAdmin) 