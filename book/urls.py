from . import views
from django.urls import path

urlpatterns = [
    path('', views.page_view, name='page_view'),
    path ('delete_booking/<int:booking_id>/', views.delete_booking, name ='delete_booking'),
     path ('update_booking/<int:booking_id>/', views.update_booking, name ='update_booking'),
    
]