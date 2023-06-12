from django.urls import path
from . import views


app_name="inventory"

urlpatterns=[

    path("add-invetory/",views.addinventorypage,name="add-inventory"),
    path("all-invetory/",views.allinventorypage,name="all-inventory"),
    path("add-inventory-process/",views.addInventoryprocess,name="add-inventory-process"),
    path("delete-inventory-process/<int:pk>/",views.deleteinventoryprocess,name="delete-inventory"),
    path("edit-inventory/<int:pk>/",views.editinventory,name='edit-inventory'),
    path("inventory-page/<int:pk>/",views.inventory_detail,name="inventory-page"),
    path("edit-inventory-process/<int:pk>/",views.editinventory_process,name='edit-inventory-process'),
]