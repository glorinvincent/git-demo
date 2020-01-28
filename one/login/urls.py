from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('details', views.details, name='details')
]