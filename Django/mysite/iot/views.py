from django.shortcuts import render
from . import iot_mqtt
from .models import Event

def index(request):
    events = Event.objects.all().order_by("-date_created")
    context = {'events' : events}
    return render(request, 'iot/index.html', context)