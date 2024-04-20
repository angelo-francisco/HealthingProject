from django.db import models
from medicine.models import Horarios
from django.contrib.auth.models import User


class Consulta(models.Model):

    status_choices = (
        ("A", "Agendada"),
        ("F", "Finalizada"),
        ("C", "Cancelada"),
        ("I", "Iniciada"),
    )
    patient = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    horario = models.ForeignKey(Horarios, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=status_choices, default="A")
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.patient.username
