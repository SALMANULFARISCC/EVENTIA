from django.shortcuts import render
from django.http import HttpResponse
from .models import event_register

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
    return render(request,"/")