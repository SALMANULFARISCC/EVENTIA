from django.urls import path

from . import views 

urlpatterns = [
    
    path("event_register" ,views.events_register, name="event_register"),

   
    ]