from django import forms
from products.models import ProductItem
from .models import Iventory


class IventoryForm(forms.ModelForm):
    class Meta:
        model=Iventory
        fields=('notes',"total_cost","total_quantity")
        widgets={"notes": forms.Textarea(  attrs={"class": "rounded-md w-[95%] border border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400 p-4","rows":4}),
                 "total_cost": forms.NumberInput(attrs={"class": "rounded-md  border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400 ","placeholder":"GH₵..."}),
                 "total_quantity": forms.NumberInput(attrs={"class": "ml-4 rounded-md  border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400 "}),
                 }


class ProductItemForm(forms.ModelForm):
    class Meta:
        model=ProductItem
        fields=("quantity", "total_price")
        widgets={
            "quantity":forms.NumberInput(attrs={"class": "rounded-md  border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400 "}),
            "total_price":forms.NumberInput(attrs={"class":"rounded-md  border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400 ","placeholder":"GH₵..."})
        }