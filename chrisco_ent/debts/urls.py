from django.urls import  path
from . import views

app_name="debt"

urlpatterns =[
    path("add-debt/",views.add_debtpage,name="add-debt"),
    path("all-debt/",views.all_debtspage,name="all-debt"),
    path('add-debt-process/',views.add_debt_process,name="add-debt-process"),  
    path("debt-details/<int:pk>/",views.debt_details,name="debt-details"),
    path("edit-debt/<int:pk>/",views.edit_debt_page,name="edit-debt"),
    path("edit-debt-process/<int:pk>/",views.edit_debt_process,name="edit-debt-process"),
    path('delete-debt/<int:pk>/',views.delete_debt,name="delete-debt")
]