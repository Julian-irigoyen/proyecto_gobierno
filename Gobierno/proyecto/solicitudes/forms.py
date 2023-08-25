from django import forms
from .models import Solicitudes

class SolicitudesForm(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = ['titulo','descripcion','solicitante',
                'fecha_solicitud','estatus']
        
        def clean(self):
            cleaned_data = super().clean()
            titulo = cleaned_data.get('titulo')
            descripcion = cleaned_data.get('descripcion')
            solicitante = cleaned_data.get('solicitante')
            fecha_solicitud = cleaned_data.get('fecha_solicitud')
            estatus = cleaned_data.get('estatus')

            if not titulo or not descripcion or not solicitante or not fecha_solicitud or not estatus:
                raise forms.ValidationError("Todos los datos debene estar completos")
            
            return cleaned_data