from . import views
from django.urls import path
urlpatterns = [
    path('', views.WelcomeList.as_view(), name='home'),
]
