from django.shortcuts import render
from events.models import event_register

# Create your views here.

def index(request):
    all_events = event_register.objects.all()
    return render(request, 'index.html' , {'events' : all_events})
