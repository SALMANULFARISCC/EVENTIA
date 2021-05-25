from django.db import models

class event_register(models.Model):
   
        title = models.CharField(max_length=100)
        organizer = models.CharField(max_length=100)
        Type = models.CharField(max_length=50)
        category = models.CharField(max_length=50)
        location = models.CharField(max_length=100)
        date = models.DateField()
        time = models.TimeField()
        poster = models.ImageField(upload_to="pics/", default="pics/default.jpg", blank=True)

class User_event_register(models.Model):
    event = models.ForeignKey(event_register, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)