"""airline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

# Table of Contents for web application:
urlpatterns = [
    path('admin/', admin.site.urls), #admin app: to use, create an admin. account...
    path('flights/', include ("flights.urls")), #go to flights.url when the path-name is /flights
    path('users/', include("users.urls")) #go to users.url and all paths in that urls.py
]


"""
$ python3 manage.py createsuperuser   [Use admin app]
  mj / spitzer.matthewjames@gmail.com / H***!M***0

"""
