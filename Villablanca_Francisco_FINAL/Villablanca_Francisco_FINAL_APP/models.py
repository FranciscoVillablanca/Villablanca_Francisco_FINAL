from django.db import models

# Create your models here.

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    ESTADO_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    fecha_inscripcion = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    hora_inscripcion = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    observacion = models.TextField(blank=True)
