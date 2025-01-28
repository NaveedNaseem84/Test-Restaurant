from . import views
from django.urls import path

urlpatterns = [
    path('', views.page_view, name='page_view'),
    path('book/', views.show_bookings, name='show_bookings'),
]