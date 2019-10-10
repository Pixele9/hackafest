from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.
def loginn(request):
    if request.method == 'POST':
        print("ES POST")
        usuario = request.POST.get('user')
        passw = request.POST.get('password')

        user = authenticate(username=usuario,password=passw)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['usuario'] = usuario
                return HttpResponse("1")
            else:
                return HttpResponse("0")
        else:
            return HttpResponse("0")
    else:
        print("ES GET")
        return render(request, "login-base.html")
    
    
def index(request):
    return render(request, "index.html")

def prediccion(request):
    return render(request, "prediccion.html")

def base(request):
    return render(request, "base.html")

def socios(request):
    return render(request, "socios.html")