from django.urls import path
from . import  views

app_name = 'auth'

urlpatterns =[
    
    path("login/",views.loginpage,name="login"),
    path("login-process/",views.loginprocess,name="login-process"),
    path("logout/",views.logout_process,name="logout"),
    path("add-user/",views.signup_page,name="add-user"),
    path("add-user-process/",views.add_user_process,name="add-user-process"),
    path("all-users/",views.view_users,name="view-users"),
    path('user-detail/',views.userpage,name='user-detail'),
    path('change-password/',views.changepasswords,name='change-password'),
    path('delete-user/<int:pk>/',views.delete_user,name='delete-user'),
    path("user-detail/<int:pk>/",views.view_details,name='view-detail'),

]