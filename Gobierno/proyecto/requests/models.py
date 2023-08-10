from django.db import models

# Create your models here.
class Solicitudes(models.Model):
    titulo = models.CharField(("Titulo"), max_length=300)
    descripcion = models.TextField(("Descripción"), default='Sin descripción', max_length=1000)
    solicitante = models.CharField(("Solicitante"), max_length=300)
    fecha_solicitud = models.DateField(("Fecha de solicitud"))

    def __str__(self):
        return self.titulo
    
