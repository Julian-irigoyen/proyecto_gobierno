from django.db import models

# Create your models here.
class Solicitudes(models.Model):
    class Meta:
        verbose_name = "Solicitudes"
        verbose_name_plural = "Solicitudes"

    PENDIENTE = 1
    APROBADA = 2
    RECHAZADA = 3

    ESTADO_CHOICES = (
        (PENDIENTE, 'Pendiente'),
        (APROBADA, 'Aprobada'),
        (RECHAZADA, 'Rechazada'),
    )

    titulo = models.CharField(("Titulo"), max_length=300)
    descripcion = models.TextField(("Descripción"), default='Sin descripción', max_length=1000)
    solicitante = models.CharField(("Solicitante"), max_length=300)
    fecha_solicitud = models.DateField(("Fecha de solicitud"))
    estatus = models.IntegerField(("Estatus"), choices=ESTADO_CHOICES)




    def __str__(self):
        return str(self.titulo)
    
