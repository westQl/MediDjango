from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def dashboard(request):
    return render(request, 'main/dashboard.html')


def main(request):
    return render(request, 'main/main.html')