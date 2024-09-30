from django.urls import path
from django.urls import path, include
from . import views 


urlpatterns = [
    path('/',views.index),
    path('contact',views.contact, name='contact'),
    path('about', views.about),
    path('students',views.students),
    
    path('students/<int:id>',views.details)
    
]