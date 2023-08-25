from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Max, Avg, Min
import json

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Solicitudes
from .forms import SolicitudesForm
from . import urls


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

class VerSolicitudes(View):
    template_name = 'solicitudes.html'

    def post(self, request):

        return render(request, self.template_name)
    @method_decorator(login_required)    

    def get(self, request):
        solicitudes = Solicitudes.objects.all()

        return render(request, self.template_name, {'solicitudes': solicitudes})

class Formulario(View):
    template_name = "crear_solicitud.html"

    def post(self, request):
        form = SolicitudesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        else:
            form = SolicitudesForm()

        return render (request, self.template_name, {'form': form})
    
    def get(self, request):
        solicitudes = Solicitudes.objects.all()
        form = SolicitudesForm()
        return render (request, self.template_name, {'form': form, 'solicitudes': solicitudes})

class EliminarSolicitud(View):
    def post(self, request, solicitud_id):
        solicitud = get_object_or_404(Solicitudes, pk=solicitud_id)
        solicitud.delete()
        return redirect('/foro')

def estadisticas_solitudes(request):

    template_name = 'estadisticas_solicitudes.html'
    #Ver el número total de solicitudes
    total_solicitudes = Solicitudes.objects.aggregate(total_solicitudes=Sum('estatus'))['total_solicitudes']

    #Ver la solicitud más antigua   
    solicitud_mas_antigua = Solicitudes.objects.aggregate(solicitud_mas_antigua=Min('fecha_solicitud'))['solicitud_mas_antigua']

    solicitud_mas_reciente = Solicitudes.objects.aggregate(solicitud_mas_reciente=Max('fecha_solicitud'))['solicitud_mas_reciente']

    return render(request, template_name, {
        'total_solicitudes' : total_solicitudes,
        'solicitud_mas_antigua' : solicitud_mas_antigua,
        'solicitud_mas_reciente' : solicitud_mas_reciente
    })

