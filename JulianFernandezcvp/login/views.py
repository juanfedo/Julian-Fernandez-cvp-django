from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('reporte_existencias')
        else:
            messages.error(request, 'El nombre de usuario o la contraseña son incorrectos.')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')