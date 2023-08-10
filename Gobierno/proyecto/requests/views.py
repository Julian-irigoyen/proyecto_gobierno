from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Solicitudes

# Create your views here.
def home(request):
    title = 'Home'
    return render(request, 'index.html', {
        'title' : title
    })

#def solicitudes(request):
#    solicitudes =  list(Solicitudes.objects.values())
#    return JsonResponse(solicitudes, safe=False)

def login(request):
    return render(request, 'login.html')

def forum(request):
    return render(request, 'requests.html')
