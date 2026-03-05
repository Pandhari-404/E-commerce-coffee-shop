from django.contrib import admin
from . models import Coffee, Contact

# Register your models here.

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    # list_display = ('name', 'price', 'quantity')

admin.site.register(Coffee, CoffeeAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address', 'date')

admin.site.register(Contact, ContactAdmin)