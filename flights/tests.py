#from django.test import TestCase
    # ^ will create a new DB for testing purposes only
from .models import Flight, Airport, Passenger
from django.db.models import Max
from django.test import Client, TestCase

# Create your tests here.

class FlightTestCase(TestCase):

    def setUp(self): # creates some sample/dummy data for the Testing Database (a special function Django knows to do first before the testing). The real data won't be touched at all in testing.
        # Create airports.
        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")
        # Create flights.
        Flight.objects.create(origin=a1, destination=a2, duration=100)
        Flight.objects.create(origin=a1, destination=a1, duration=200)
        Flight.objects.create(origin=a1, destination=a2, duration=-100) # -100 minutes?!

    def test_departures_count(self): # are we properly counting all departures in the DB?
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(), 3)
        # ^ are City A's departures == 3?

    def test_arrivals_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 1) # 1 arrival at city A?

    def test_valid_flight(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = Flight.objects.get(origin=a1, destination=a2, duration=100) # get the flight
        self.assertTrue(f.is_valid_flight()) # flight should be valid... is it? Yes: duration > 0; origin != destination


    def test_invalid_flight_destination(self):
        a1 = Airport.objects.get(code="AAA")
        f = Flight.objects.get(origin=a1, destination=a1)
        self.assertFalse(f.is_valid_flight()) # This should NOT be a valid flight?


    def test_invalid_flight_duration(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = Flight.objects.get(origin=a1, destination=a2, duration=-100) # duration = -100min?!
        self.assertFalse(f.is_valid_flight()) #should be False (and pass the assertFalse test...)



    def test_index(self):
        # Set up client to make requests
        c = Client()
        # Send get request to index page and store response
        response = c.get("/flights/")
        # Make sure status code is 200
        self.assertEqual(response.status_code, 200) #200=OK
        # Make sure three flights are returned in the context
        self.assertEqual(response.context["flights"].count(), 3) # we pass in 3 results in the context ... check that!
            # Context: Python dictionary passed in when we return render(template)...


    def test_valid_flight_page(self):
        a1 = Airport.objects.get(code="AAA")
        f = Flight.objects.get(origin=a1, destination=a1)
        c = Client()
        response = c.get(f"/flights/{f.id}") # a valid ID:
        self.assertEqual(response.status_code, 200) #: should be OK(200)

    def test_invalid_flight_page(self):
        max_id = Flight.objects.all().aggregate(Max("id"))["id__max"]
        c = Client()
        response = c.get(f"/flights/{max_id + 1}") #an invalid ID (1 beyond the max_id)
        self.assertEqual(response.status_code, 404) #should return a status code 404: flight doesn't exist!




    def test_flight_page_passengers(self):
        f = Flight.objects.get(pk=1)
        p = Passenger.objects.create(first="Alice", last="Adams")
        f.passengers.add(p)
        #
        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["passengers"].count(), 1) #


    def test_flight_page_non_passengers(self):
        f = Flight.objects.get(pk=1)
        p = Passenger.objects.create(first="Alice", last="Adams")

        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["non_passengers"].count(), 1)
