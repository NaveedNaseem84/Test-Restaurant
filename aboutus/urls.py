from . import views
from django.urls import path
urlpatterns = [
   # path('', views.About.as_view(), name='about'),
    path('', views.about_me, name='about'),
]
