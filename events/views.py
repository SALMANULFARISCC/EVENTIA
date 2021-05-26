from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import event_register,User_event_register

from django.views.generic import FormView, CreateView
from .forms import eventregisterform




def events_register(request):
    form = eventregisterform()
    
    if request.method == 'POST' :
        title = request.POST.get("title")
        organizer = request.POST.get("organizer")
        Type = request.POST.get("Type")
        location = request.POST.get("location") 
        date = request.POST.get("date")
        time = request.POST.get("time")
        poster = request.POST.get("avatar") 
       
        events_register = event_register(title=title,organizer=organizer,Type=Type,location=location,date=date,time=time,poster=poster)
        events_register.save()
        return redirect('index')
    context = {'form': form}
    return render(request,"event_register.html", context)

def register_for_event(request):
    if request.method == 'POST' :
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")

        register_for_event = User_event_register(first_name=first_name,last_name=last_name,email=email)
        register_for_event.save()
        return redirect('index')
 
    return render(request,"register_for_event.html")