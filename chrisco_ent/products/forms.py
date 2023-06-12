from .models import  *
from  django  import  forms


class ProductForm(forms.ModelForm):
    class  Meta:
        model=Product
        fields=("name","notes")
        widgets={
            "name":forms.TextInput(attrs={"class": "h-12 rounded-md w-[95%] border border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400 "}),
            "notes":forms.Textarea(attrs={"class":"rounded-md w-[95%] border border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400 p-4","rows":4}),

        }

class PriceForm(forms.ModelForm):
    class Meta:
        model=Price
        fields=("price",)
        widgets={
            'price': forms.NumberInput(attrs={"class":"h-12 rounded-md w-[95%]  border border-gray-400 focus:outline-none focus:ring-0 focus:border-gray-400" ,"placeholder":"GH₵..."})
        }