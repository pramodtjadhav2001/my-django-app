from django.contrib import admin
from django.urls import path
from myadmin import views
urlpatterns = [
    path('',views.admin),
    path('admin_home/',views.admin_home),
    path('save_home/',views.save_home),


    path('pizza/',views.pizza),
    path('save_pizza/',views.save_pizza),
    path('delete_pizza/',views.delete_pizza),
    path('pizza_edit/',views.pizza_edit),
    path('update_pizza/',views.update_pizza),
    


    path('salads/',views.salads),
    path('save_salads/',views.save_salads),
    path('delete_salads/',views.delete_salads),
    path('salads_edit/',views.salads_edit),
    path('update_salads/',views.update_salads),



    path('starter/',views.starter),
    path('save_starter/',views.save_starter),
    path('delete_stater/',views.delete_stater),
    path('edit_starter/',views.edit_starter), 
    path('update_starter/',views.update_starter),


    path('c_info/',views.c_info),
    path('save_admin_contact/',views.save_admin_contact),
    path('save_contact/',views.save_contact),





    path('admin_contact/',views.admin_contact),
    path('delete_contact/',views.delete_contact),
    path('edit_contact/',views.edit_contact),
    path('update_contact/',views.update_contact),



    path('about_info/',views.about_info),
    path('save_about_info/',views.save_about_info),
    
    path('day/',views.day),
    path('save_day/',views.save_day),


   path('registraion/',views.registraion),
   path('save_admin_reg/',views.save_admin_reg),

   path('login/',views.login),
   path('save_login/',views.save_login)


]