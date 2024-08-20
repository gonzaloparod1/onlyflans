from django.urls import path
from . import views

urlpatterns = [
    path('', views.indice, name="indice"),
    path('acerca/', views.acerca, name="acerca"),
    path('bienvenido/', views.bienvenido, name="bienvenido"),
    path('exito', views.exito, name="exito"),
    path('nueva', views.nueva_vista),
    path('contacto', views.contacto, name="contacto"),
    path('detalle/<uuid:flan_uuid>', views.detalle_flan, name='detail_flan'),
    path('profile/', views.profile_view, name='profile'),
    path('profile_exito', views.profile_exito, name='profile_exito'),
    # path('favorite-int', views.favorites, name="fav"),
    #* <!-- apply CONTACT FORM url --> 
]