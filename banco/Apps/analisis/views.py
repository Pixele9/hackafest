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








# FUNCION QUE AGREGO A LOS ALUMNOS DEL EXCEL HACIA LA BASE DE DATOS.
# SE ELIMINO POR QUE SOLO SE USO UNICAMENTE PARA SUBIR LOS ALUMNOS A LA BASE DE DATOS
# def pruebaAlumnos(request):
#     alumnos = resultados.b['data'] 
#     contadorAlumno = 1

#     for alumno in alumnos:
#         nombre = alumno['NOMBRE']  
#         bachillerato = alumno['BACHILLERATO']  
#         aceptado = alumno['ACEPTADO']
#         carrera = alumno['CARRERA']
#         # NOMBRE Y APELLIDOS
#         nombres = nombre.split()
#         contador = len(nombres)
#         nombre = ""
#         for x in range(2,contador):
#             nombre+= nombres[x]+ " "

#         # BACHILLERATO
#         if "UAQ" in bachillerato:
#             bachillerato = 1
#         else:
#             bachillerato = 0

#         # ACEPTADO
#         if "S" in aceptado:
#             aceptado = 1
#         else:
#             aceptado = 0

#         # CARRERA
#         carreras = Carrera.objects.all()
#         c=0
        
#         if "SOFTWARE" in carrera:
#             c = carreras.get(nombre__icontains="software")
#         elif "INFORMATICA" in carrera:
#             c = carreras.get(nombre__icontains="informática")
#         elif "INFORMACION" in carrera:
#             c = carreras.get(nombre__icontains="administración")
#         elif "COMPUTACION" in carrera:
#             c = carreras.get(nombre__icontains="computación")
#         elif "TELECOMUNICACIONES" in carrera:
#             c = carreras.get(nombre__icontains="telecomunicaciones")

#         folio = contadorAlumno
#         contadorAlumno = contadorAlumno+1
#         nombre = nombre
#         apellidos = nombres[0] + " " + nombres[1]
#         aciertosTotales = alumno['Resultado']
#         genero = alumno['GENERO']
#         bachillerato = bachillerato
#         aceptado = aceptado
#         p = Periodo.objects.get(id=1)
#         print(folio, nombre, apellidos, aciertosTotales, genero, bachillerato, aceptado)

#         objeto_alumno = Alumno(folio=folio, nombre=nombre, apellidos=apellidos,aceptado=aceptado, aciertosTotales=aciertosTotales, genero=genero, bachillerato=bachillerato, carrera=c, periodo=p)
#         objeto_alumno.save()

#     return HttpResponse('Hola')


    
def index(request):
    return render(request, "index.html")

def prediccion(request):
    return render(request, "prediccion.html")

def base(request):
    return render(request, "base.html")

def socios(request):
    return render(request, "socios.html")

def miPerfil(request):
    return render(request, "miPerfil.html")