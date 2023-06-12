from django.contrib import admin
from .models import Iventory
from products.models import ProductItem

# Register your models here.
class ProductInline(admin.TabularInline):
    model = Iventory.products.through  # through model for the ManyToMany relationship
    extra = 0 # Number of empty forms to display

class InventoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

admin.site.register(Iventory,InventoryAdmin)