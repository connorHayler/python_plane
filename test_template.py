import unittest
import json
import pytest
from passenger import Passenger

class Testing(unittest.TestCase):
    passenger = Passenger("fName", "lName", "passportID")
    flight = Flight("origin", "destination", "vehicle", "departure time")
    passenger.add()
    def test_passenger_create(self):
        self.assertIsInstance(self.passenger, Passenger)
        self.assertIsNotNone(self.passenger.f_name)
        with open("passenger_records.json", "r") as file:
            json_file = json.load(file)
            passenger_json = json_file["passenger"]
            for person in passenger_json:
                if person["passport"] == "passportID":
                    id = person["fName"]
                    break
            self.assertEquals(id, "fName")

    def test_flight_trip(self):
        self.assertIsInstance(self.flight, Flight)
        with open("flight_records.json") as file:
            json_file = json.load(file)
            flight_json = json_file["flight"]
            for flight in flight_json:
                if flight["flightID"] == "FlightID":
                    destination = flight["destination"]
                    break
            self.assertEquals(destination, "destination")




