from django.contrib import admin  
from django.urls import path  
from meroshare import views  

urlpatterns = [    
    path('',views.show),
    path('add', views.add), 
    path('edit/<str:id>', views.edit),  
    path('update/<str:id>', views.update),  
    path('delete/<str:id>', views.delete),  
]  