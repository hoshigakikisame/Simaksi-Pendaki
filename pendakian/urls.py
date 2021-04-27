from django.urls import path 
from . import views

urlpatterns = [
	path('solo/', views.daftar_solo, name="solo"),
	path('group/', views.daftar_group, name="group"),
]