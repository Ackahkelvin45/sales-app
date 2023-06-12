from django.urls import path

from . import views



app_name = 'sales'

urlpatterns =[
    path("",views.index,name="index"),
    path("add-sales/",views.addsalespage,name="add-sales"),
    path("all-sales/",views.allsalespage,name="all-sales"),
    path("add-sales-process/",views.addsalesprocess,name='add-sales-process'),
    path("sale-details/<int:pk>/",views.salesdetailpage,name="sale-details"),
    path("download-details/<int:pk>/",views.download_sale,name='download-sale'),
    path("delete-sales/<int:pk>/",views.delete_sale,name='delete-sale'),
    path("edit-sale/<int:pk>/",views.edit_sales,name='edit-sale'),
    path("edit-sale-process/<int:pk>/",views.edit_sales_process,name='edit-sale-process'),

]