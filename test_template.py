import unittest
import json

class Testing(unittest.TestCase):
    passenger = Passenger("fName", "lName", "passportID")
    def test_passenger_create(self):
        self.assertIsInstance(passenger, Passenger)
        self.assertIsNotNone(passenger.f_name)
        with open("passenger_records.json", "r") as file:
            json_file = json.load(file)
            passenger_json = json_file["passenger"]
            for person in passenger_json:
                if person["passportNumber"] == "passportID":
                    id = person["passportNumber"]
            self.assertEquals(id, "passportID")
