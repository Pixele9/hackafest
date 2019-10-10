from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from twilio.rest import Client
from django.conf import settings

import urllib3, requests, json

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

def base(request):
    return render(request, "base.html")

def socios(request):
    return render(request, "socios.html")

def prediccion(request):
    return render (request, "prediccion.html")

def getPrediction(request):
    edad = request.POST.get("edad")
    genero = request.POST.get("genero")
    mesEntrega = request.POST.get("mesEntrega")
    ocupacion = request.POST.get("ocupacion")
    municipio = request.POST.get("municipio")

    print(edad, genero, mesEntrega, ocupacion, municipio)
    iam_token = "eyJraWQiOiIyMDE5MDcyNCIsImFsZyI6IlJTMjU2In0.eyJpYW1faWQiOiJpYW0tU2VydmljZUlkLWE3YzQ3NDNkLTQyMmMtNDc2MS1hN2E1LTVjMGJiNWRlMDdkNSIsImlkIjoiaWFtLVNlcnZpY2VJZC1hN2M0NzQzZC00MjJjLTQ3NjEtYTdhNS01YzBiYjVkZTA3ZDUiLCJyZWFsbWlkIjoiaWFtIiwiaWRlbnRpZmllciI6IlNlcnZpY2VJZC1hN2M0NzQzZC00MjJjLTQ3NjEtYTdhNS01YzBiYjVkZTA3ZDUiLCJzdWIiOiJTZXJ2aWNlSWQtYTdjNDc0M2QtNDIyYy00NzYxLWE3YTUtNWMwYmI1ZGUwN2Q1Iiwic3ViX3R5cGUiOiJTZXJ2aWNlSWQiLCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiIxNGE5YmNhMDk2N2Q0NTkzODM4ZjE3MzkyNmVjZjU0YSJ9LCJpYXQiOjE1NzA3MjU2MjIsImV4cCI6MTU3MDcyOTIyMiwiaXNzIjoiaHR0cHM6Ly9pYW0uY2xvdWQuaWJtLmNvbS9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOmFwaWtleSIsInNjb3BlIjoiaWJtIG9wZW5pZCIsImNsaWVudF9pZCI6ImJ4IiwiYWNyIjoxLCJhbXIiOlsicHdkIl19.YOIBbBMJkvZUhh4VV2V9981ZO64wLZx5gddxUiXDEuKdVBiK5sEOwxQsS40W9qjpF5tel1LabRv_HHLsEcBek_TIPtFcLIoozOnePgrs6INzZ-XhbkX3WNFUoyGlFOuM0ZjULu-2nyM8ze-vpxx-H32E-pG0KpnjOG5-JoDZK4PoXghXTjIE7_CNYqJR1khoWDRnlQdw2xJOo5Hyxt48T-7uNv0FLbgwHiqaoWntH1O9eCyWBGzf4-07tKrsp74MRrO90udE-0tSR8itrXCbHPrGFL-Ro8YSv-KFS4Qrngl-tzmjXkiYRVR0rfuCZS7GW6UCLjZj6py6OmXjkyQLFA"
    ml_instance_id = "f6fa9907-1416-4413-ae21-1da86e425b99"

    # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}

    # NOTE: this will be the value I will have to take from the form
    array_of_values_to_be_scored = [municipio,int(edad),genero,ocupacion,int(mesEntrega)]


    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"fields": ["MUNICIPIO", "EDAD", "SEXO", "OCUPACION", "MESDEENTREGA"], "values": [array_of_values_to_be_scored]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v3/wml_instances/f6fa9907-1416-4413-ae21-1da86e425b99/deployments/5acaf946-88ae-4184-8cf5-78361d60688c/online', json=payload_scoring, headers=header)
    prediction = json.loads(response_scoring.text)["values"][0][0]
    print("Scoring response:")
    print(prediction)
    return HttpResponse(prediction)
