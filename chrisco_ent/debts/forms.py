from django import forms
from  .models import Debt 
from  products.models import Product


class DebtForm(forms. ModelForm):
   

    class Meta:
        model=Debt
        fields=['notes','customer_name']
    
        widgets={
                        'notes': forms.Textarea(attrs={"class":" rounded-md w-[95%] border border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400 p-4","rows":4}),
            "customer_name":forms.TextInput(attrs={"class": "h-12 rounded-md w-[95%]  border border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400"}), 
        }