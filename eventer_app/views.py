from django.shortcuts import render
from .events import events
from datetime import datetime

# Create your views here.
def index_view(requets):
    current_day = datetime.now().day
    current_event = events[current_day]
    client_ip = requets.META.get('REMOTE_ADDR')

    context = {
        'current_day': current_day,
        'current_event': current_event,
        'client_ip': client_ip,
        'events': events
    }

    return render(requets, 'index.html', {})