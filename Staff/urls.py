from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('entry/', views.entrydetails, name='entrydetails'),
    path('admin/', admin.site.urls),
    path('update_details/<int:id>/', views.update_details, name='update_details'),
    path('delete_details/<int:id>/', views.delete_details, name='delete_details'),
]
