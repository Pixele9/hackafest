"""banco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Apps.analisis import views as viewsBanco

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', viewsBanco.index, name="index"),
    path('login/', viewsBanco.loginn, name='login' ),
    path("base/", viewsBanco.base, name="base"),
    path('prediccion/', viewsBanco.prediccion , name='prediccion'),
    path("socios/", viewsBanco.socios, name="socios"),
    path("mensaje/", viewsBanco.mensaje, name="mensaje"),
    path('miPerfil/', viewsBanco.miPerfil, name="miPerfil")
]
