from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('reporte_existencias')
        else:
            message = 'El nombre de usuario o la contraseña son incorrectos.'
    else:
        message = ''
    return render(request, 'login.html', {'message': message})

def user_logout(request):
    logout(request)
    return redirect('login')