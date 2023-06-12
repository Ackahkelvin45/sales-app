from django.db import models
from products.models import ProductItem
from  sales.models import Sales
from authentication.models import User

# Create your models here.

PAID=(
  ("True","True"),
  ("False","False"),

)

class Debt (models.Model):
    sale=models.OneToOneField(Sales,null=True,blank=True,on_delete=models.PROTECT,related_name='sale_debt')
    customer_name=models.CharField(max_length=100,blank=True,null=True)
    serial_number=models.CharField(max_length=20,null=True, blank=True)
    total_price=models.DecimalField(null=True, blank=True,decimal_places=2,max_digits=100)
    notes=models.TextField(null=True, blank=True,max_length=300)
    paid_price=models.DecimalField(null=True, blank=True, decimal_places=2,max_digits=100)
    due_price=models.DecimalField(null=True, blank=True, decimal_places=2,max_digits=100)
    created_by=models.ForeignKey(User,null=True, blank=True,on_delete=models.PROTECT,related_name="recorder")
    paid=models.CharField(choices=PAID,null=True,blank=True,max_length=20,default='False')
    created_date=models.DateTimeField(auto_now_add=True,null=True,blank=True) 
 

    def __str__(self):
        return self.notes

