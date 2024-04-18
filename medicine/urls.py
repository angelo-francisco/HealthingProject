from django.urls import path
from medicine import views

urlpatterns = [
    path("auth/", views.auth_doctor, name='auth_doctor'),
]
