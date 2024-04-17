from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.messages import constants


def auth_login(request):
    if request.method == "GET":
        return render(request, "user_auth/login.html")

    else:
        return redirect(reverse("auth_login"))


def auth_signup(request):
    if request.method == "GET":
        return render(request, "user_auth/signup.html")

    else:
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["senha"]
        password_conf = request.POST["confirmar_senha"]

        user = User.objects.filter(username=username)

        if not user.exists():
            if password == password_conf:
                User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=make_password(password),
                )

                messages.add_message(request, constants.SUCCESS, "Dados Cadastrados!")
                return redirect(reverse("auth_login"))

            messages.add_message(request, constants.WARNING, "As senhas não coincidem!")
            return redirect(reverse("auth_signup"))

        messages.add_message(request, constants.ERROR, "Username em utilização!")
        return redirect(reverse("auth_signup"))


def auth_logout(request):
    pass