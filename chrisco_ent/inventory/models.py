from django.db import models

# Create your models here.
from django.db import models
from products.models import ProductItem,Product

class Iventory(models.Model):
    notes=models.CharField(max_length=500,null=True, blank=True)
    products=models.ManyToManyField(ProductItem,related_name="products")
    total_cost=models.DecimalField(null=True, decimal_places=2,blank=True,max_digits=100)
    total_quantity=models.IntegerField(null=True, blank=True,)
    new_total_cost=models.DecimalField( decimal_places=2,max_digits=100,blank=True,null=True)
    new_total_quantity=models.IntegerField(null=True,blank=True)
    serial_number=models.CharField(max_length=20,null=True, blank=True)    
    created=models.DateField(null=True, blank=True,auto_now_add=True)

    def save2(self, *args, **kwargs):
       
        self.new_total_quantity = self.total_quantity
        self.new_total_cost=self.total_cost
        super().save(*args, **kwargs)


    def __str__ (self):
        return self.notes 

