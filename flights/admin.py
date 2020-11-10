from django.contrib import admin
from .models import Flight, Airport, Passenger #all models.py classes


#Configuration customization:
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")
# Django configuration!
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)


# Register your models here.

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin) #** use FlightAdmin settings!
admin.site.register(Passenger, PassengerAdmin) #

"""
$ python3 manage.py createsuperuser   [Use admin app]
  mj / spitzer.matthewjames@gmail.com / H***!M***0

$ python3 manage.py runserver
   http://127.0.0.1:8000/admin/
   - Login using admin credentials to use web-server interface
      to easily add Flights & Airports, rather than using the command-airline
      Django shell...

"""
