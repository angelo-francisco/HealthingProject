from django.urls import path
from medicine.views import *

urlpatterns = [
    path("sign_doctor/", auth_doctor, name="auth_doctor"),
    path("horarios/", horarios, name="horarios"),
    path("consultas/", medico_consultas, name="medico_consultas"),
]
