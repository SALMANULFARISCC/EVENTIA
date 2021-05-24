from django.shortcuts import render
from django.http import HttpResponse
from .models import event_register,User_event_register


def events_register(request):
    if request.method == 'POST' :
        title = request.POST.get("title")
        organizer = request.POST.get("organizer")
        Type = request.POST.get("Type")
        location = request.POST.get("location") 
        date = request.POST.get("date")
        time = request.POST.get("time")
        poster = request.POST.get("poster") 

        events_register = event_register(title=title,organizer=organizer,Type=Type,location=location,date=date,time=time,poster=poster)
        events_register.save()
        
     
    return render(request,"event_register.html")

def register_for_event(request):
    if request.method == 'POST' :
        first_name = request.POST.get("title")
        last_name = request.POST.get("title")
        email = request.POST.get("title")

        register_for_event = User_event_register(first_name=first_name,last_name=last_name,email=email)
        register_for_event.save()
        

    return render(request,"register_for_event.html")