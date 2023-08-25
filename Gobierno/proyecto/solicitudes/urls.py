from django.urls import path
from . import views

urlpatterns = [
#    path('solicitudes/', views.solicitudes),
    path('inicio/', views.home, name="inicio"),
    path('foro/', views.VerSolicitudes.as_view(), name="foro"),
    path('crear-solicitud/', views.Formulario.as_view(), name="crear-solicitud"),
    path('eliminar-solicitud/<int:solicitud_id>/', views.EliminarSolicitud.as_view(),name='eliminar_solicitud'),
    path('estadisticas/', views.estadisticas_solitudes, name='estadisticas_solicitudes')
]