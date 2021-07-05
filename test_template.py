import unittest
import json
import pytest
from passenger import Passenger
from vehicle import Vehicle
from flight import Flight

class Testing(unittest.TestCase):
    plane = Vehicle("planeID", "Plane", "total passenger", "age")
    passenger = Passenger("fName", "lName", "passportID")
    flight = Flight("origin", "destination", plane, "departure time")
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
        with open("flight_records.json", "r") as file:
            json_file = json.load(file)
            flight_json = json_file["flight"]
            for flight in flight_json:
                if flight["flightID"] == "FlightID":
                    destination = flight["destination"]
                    break
            self.assertEquals(destination, "destination")

    def test_vehicle(self):
        with open("vehicle_records.json", "r") as file:
            json_file = json.load(file)
            vehicle_json = json_file["vehicles"]
            for vehicle in vehicle_json:
                if vehicle["id"] == "testID":
                    self.assertEquals(vehicle["passengers"], 32)
                    break






