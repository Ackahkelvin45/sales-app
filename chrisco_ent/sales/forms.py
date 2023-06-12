from django import forms
from .models import Sales



class SalesForm(forms.ModelForm):
    class Meta:
        model=Sales
        fields=('notes','customer_name','total_price','paid_price','due_price')
        widgets={
            'notes': forms.Textarea(attrs={"class":" rounded-md w-[95%] border border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400 p-4","rows":4}),
            "customer_name":forms.TextInput(attrs={"class": "h-12 rounded-md w-[95%]  border border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400"}), 
            "total_price":forms.NumberInput(attrs={"class": "h-12 rounded-md w-[95%]  border border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400","placeholder":"GH₵...","step":"0.01","value":"0"}),
            "paid_price":forms.NumberInput(attrs={"class": "h-12 rounded-md w-[95%]  border border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400","placeholder":"GH₵...","step":"0.01","id":"paid_price","value":"0"} ),
            "due_price":forms.NumberInput(attrs={"class": "h-12 rounded-md w-[95%]  border border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400","placeholder":"GH₵...","step":"0.01" ,"value":"0" }), 
        }


