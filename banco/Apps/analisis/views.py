from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from twilio.rest import Client
from django.conf import settings

# Create your views here.
def loginn(request):
    if request.method == 'POST':
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
        return render(request, "login-base.html")
    
def mensaje(request):
    to = '+527331366904'
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(
        body='Hello testing twilio in Django', 
        to=to, from_=settings.TWILIO_PHONE_NUMBER)

    return HttpResponse("Hola")

    
def index(request):
    return render(request, "index.html")

def prediccion(request):
    return render(request, "prediccion.html")

def base(request):
    return render(request, "base.html")

def socios(request):
    return render(request, "socios.html")