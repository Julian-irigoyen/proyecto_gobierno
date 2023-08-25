from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout

def custom_logout(request):
    logout(request)
    return redirect('/inicio')

def custom_login(request):
    template_name = 'login.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('------------------> Si entro al login')
            return redirect('/inicio')
        else:
            print('------------------> No entro al login')
            messages.error(request, 'Credenciales inválidas')
            return render(request, 'login.html')

    return render(request, template_name)


