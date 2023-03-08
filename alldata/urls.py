
from django.contrib import admin
from django.urls import path,include
from alldata import views

urlpatterns = [
    path('',views.loginaction),
    path('signup/',views.signupaction),
    path('homepage/',views.homepage),
    path('new_contact/',views.create_new_contact),
    path('profile_details/<int:value>',views.detailpage,name="productdetails"),
    path('edit_contact/<int:pk>',views.editprofile,name="editprofile"),
    path('delete/<int:pk>',views.deleteprofile,name="deleteprofile"),
    path('deletebyid/<int:pk>',views.deleteprofilebyid,name="deleteprofilebyid"),

    ]
