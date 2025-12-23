from django.shortcuts import render
from django.utils.timezone import localtime, now
from .models import Event

def countdown_timer(request):
    event = Event.objects.latest('id')   # your event model
    event_time = localtime(event.event_date)
    current_time = now()
    
    if event_time > current_time:
        delta = event_time - current_time
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
    else:
        days = hours = minutes = seconds = 0

    return render(request, "myapp.html", {
        "data": {
            "name": event.name,
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }
    })