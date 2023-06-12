from django.db import models

# Create your models here.




class Price(models.Model):
    price=models.DecimalField(decimal_places=2,null=True,blank=True,max_digits=20)
    created=models.DateField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return str(self.price )

class Product(models.Model):
    name=models.CharField(max_length=30,unique=True,null=True,blank=True)
    price=models.ForeignKey(Price,null=True,blank=True,on_delete=models.CASCADE)
    serial_number=models.CharField(max_length=100,unique=True,null=True,blank=True)
    notes=models.TextField(max_length=200,null=True,blank=True)
    created=models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name 



class ProductItem(models.Model):
    product=models.ForeignKey(Product, null=True, blank=True,on_delete=models.SET_NULL)
    quantity=models.IntegerField(null=True, blank=True)
    total_price=models.DecimalField(decimal_places=2,max_digits=100,null=True,blank=True)
    new_quantity=models.IntegerField(null=True, blank=True)
    new_total_price=models.DecimalField(decimal_places=2,max_digits=100, null=True)


    def save2(self, *args, **kwargs):
       
        self.new_quantity = self.quantity
        self.new_total_price=self.total_price
        super().save(*args, **kwargs)

    def __str__(self):
        return "price:"+ str(self.total_price)+ " quantity:"+ str(self.quantity)  +  "  id: "+str(self.id)



   