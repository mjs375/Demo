from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse #Takes name="..." of particular VIEW and gives back the actual URL path (just helpful so I don't have to hard-code the URL so much... easier to change later)

# Create your views here.


def index(request):
    #Display a list of all Flight (objects)
        # remember the CONTEXT is a DICT{key:value, key:value}
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
        # "flights" is the variable name we give it to access in the html
        # Flight.objects.all() attaches the Python-Django for the variable
    })


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id) #pk=pprimary key / id
    ## ADD ERROR CHECKING: if the user tries to access some flight-url that doesn't exist, e.g. flight/28...
    passengers = flight.passengers.all(), #gives access to related_name passengers
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    # ^^for drop-down of all passengers NOT already in flight...^^
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })



def book(request, flight_id):
    if request.method == "POST": # for a POST request, add a new flight
        flight = Flight.objects.get(pk=flight_id)
            #^^access the flight
        passenger_id = int(request.POST["passenger"])
            #^^find the passenger ID from the submitted form data
        passenger = Passenger.objects.get(pk=passenger_id)
            #^^find the passenger based on the id

        ## ERROR CHECKING: what if passenger doesn't exist, &c.

        passenger.flights.add(flight) #adding a new row to table... puts passenger in flight
        # Redirect user to flight page
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
    #else: #GET
        #return render(request, "flights/flight.html")







#
