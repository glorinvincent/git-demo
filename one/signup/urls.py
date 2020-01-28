from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('adduser', views.adduser, name='adduser'),
    path('stud_details', views.stud_details, name='stud_details')
]