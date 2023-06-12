from django.urls import path
from . import views


app_name="products"

urlpatterns=[

    path("add-product/",views.addproductspage,name="add-products"),
    path("add-product-process/",views.addproductprocess,name="add-product-process"),
    path("product-edit/<int:pk>/",views.editproductspage,name="edit-product"),
    path("all-products/",views.allproductspage,name="all-products"),
    path("delete-product/<int:pk>/",views.deleteproduct,name="delete-product"),
    path("product-detail/<int:pk>/",views.productdetail,name="product-detail"),
    path("edit-product-process/<int:pk>/",views.editproductprocess,name="edit-product-process"),


]