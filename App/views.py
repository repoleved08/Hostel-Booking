from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Hostel
from django.http import HttpResponse

# Create your views here.
def index(request):
    hostels = Hostel.objects.all()
    return render(request, 'index.html', {'hostel': hostels})