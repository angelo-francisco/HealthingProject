from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url=reverse('auth_login'))
def auth_doctor(request):
    if request.method == "GET":
        return render(request, 'medicine/')
