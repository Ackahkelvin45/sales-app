from django.urls import path
from . import views

app_name='report'

urlpatterns =[
    path('inventory-report',views.inventoryreportpage, name='inventoyreportpage'),
    path('business-report',views.businessIventorypage, name='businessreportpage'),
       
]