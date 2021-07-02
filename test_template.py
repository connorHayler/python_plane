import unittest
import json

class Testing(unittest.TestCase):
    passenger = Passenger("fName", "lName", "passportID")
    def test_passenger_create(self):
        self.assertIsInstance(passenger, Passenger)
        self.assertIsNotNone(passenger.f_name)
        with open("passenger_records.json", "r") as file:
            json_file = json.load(file)
            id = json_file["passportID"]
            self.assertEquals(id, "passportID")
