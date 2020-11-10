"""
*Every time* we make changes in models.py, we have to (to make the changes in the DB)
    a) make migrations and b) migrate.
a)   $ python3 manage.py makemigrations     [Check for changes in models.py]
b)   $ python3 manage.py migrate            [Apply changes]
"""
###
"""
Django-Python Shell:
$ python3 manage.py shell
$ from flights.models import *
...
$ quit()
"""
###
"""
Run SQL commands:
$ sqlite3 flights.sql
sqlite3>
...>

COMMANDS:
.mode columns   [Change settings to make output readable]
.headers yes    [Change settings...""]
. tables   [List all current tables]
SELECT * FROM table_name;
.quit [Exit SQL prompt]
"""

from django.db import models

# Create your models here. Every model is a Python Class.





############################
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"



###########################
class Flight(models.Model): #inherits from models.model
    # Every flight has an Origin, Destination, Duration
        #origin = models.CharField(max_length=64)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
            # on_delete: if the particular Airport is deleted, also delete any flights connected to that airport
            # related_name: gives us a way to search for all flights with a given airport as their origin/destination.
        #destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self): #if this fx returns a string representation of the model...:
        return f"{self.id}: {self.origin} to {self.destination}"

    def is_valid_flight(self): # TEST: is this a valid flight?
        # return self.origin != self.destination or self.duration > 0 #Bug found with tests.py: shouldn't be OR, the flight should pass BOTH tests to be valid
        return self.origin != self.destination and self.duration > 0 # BUG HERE!!!


   
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
        #blank=True: passengers can be registered to no flights
        #related_name: if I have a passenger, can use Flight attribute to access all their Flights

    def __str__(self): #string representation–
        return f"{self.first} {self.last}"





#
