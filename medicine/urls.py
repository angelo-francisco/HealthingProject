from django.urls import path
from medicine.views import *

urlpatterns = [
    path("sign_doctor/", auth_doctor, name='auth_doctor'),
]
