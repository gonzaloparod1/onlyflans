from django.urls import path
from . import views

urlpatterns = [
    path('', views.indice, name="indice"),
    path('acerca/', views.acerca, name="acerca"),
    path('welcome/', views.bienvenido, name="bienvenido"),
    path('exito/', views.exito, name="exito"),
    path('nueva/', views.nueva_vista),
    path('contacto/', views.contacto, name="contacto"),
    #* <!-- apply CONTACT FORM url --> 
]
