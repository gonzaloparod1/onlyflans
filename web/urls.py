## app web - urls
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.home),
    path('about/', views.acerca),
    path('welcome/', views.bienvenido),
    path('', include('web.urls'))
    ]