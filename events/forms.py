from django.forms import ModelForm
from .models import event_register

class  eventregisterform(ModelForm):
     class Meta:
         model = event_register 
         fields = ['poster']
