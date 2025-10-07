from django.shortcuts import render
from django.http import HttpResponse
from .models import LogEntry

# Create your views here.

def log_list(request):
    entries = LogEntry.objects.all().order_by('-logged_date')
    context = {
        'entries': entries,
    }
    return render(request, 'media/log_list.html', context)