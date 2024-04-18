from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login/')
def auth_doctor(request):
    if request.method == "GET":
        return render(request, 'medicine/auth_doctor.html')
    
    else:
        return redirect(reverse('auth_doctor'))
