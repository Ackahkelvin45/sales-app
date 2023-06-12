from django.db import models
from products.models import ProductItem
from  authentication.models import  User
from inventory.models  import Iventory


# Create your models here.


DEBT=(
  ("True","True"),
  ("False","False"),

)

class  Sales(models.Model):
    customer_name=models.CharField(max_length=100,null=True,blank=True)
    products=models.ManyToManyField(ProductItem,blank=True,related_name='products_sales')
    total_price=models.DecimalField(null=True, blank=True,decimal_places=2,max_digits=100)
    total_quantity=models.IntegerField(null=True, blank=True)
    notes=models.TextField(null=True, blank=True,max_length=300)
    paid_price=models.DecimalField(null=True, blank=True, decimal_places=2,max_digits=100)
    due_price=models.DecimalField(null=True, blank=True,decimal_places=2,max_digits=100)
    serial_number=models.CharField(null=True,blank=True,max_length=20)
    created_by=models.ForeignKey(User,null=True, blank=True,on_delete=models.PROTECT,related_name="creator")
    created_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)  
    debt=models.CharField(choices=DEBT,null=True,blank=True,max_length=20,default='False')
    inventory=models.ForeignKey(Iventory,null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.customer_name 

