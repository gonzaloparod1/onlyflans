from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio),
    path('acerca/', views.acerca)
]
