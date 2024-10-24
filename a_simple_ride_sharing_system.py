# -*- coding: utf-8 -*-
"""A Simple Ride-Sharing System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G--_dxsPOr4hlkWtKzF1LxYMF_95dCC0
"""
import math
# Location class that represents x, y coordinates
class Location():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

# Car class to represent each car, with a name, location, and cost per mile
class Car():
    def __init__(self, car_name, location, cost_per_mile):
        self.car_name = car_name
        self.location = location
        self.cost_per_mile = cost_per_mile

    def __str__(self):
        return f'[{self.car_name}, {self.location}, {self.cost_per_mile}]'

    # Method to update car location
    def move_to(self, new_x, new_y):
        self.location = Location(new_x, new_y)

# Passenger class representing each passenger with a name and location
class Passenger():
    def __init__(self, passenger_name, location):
        self.passenger_name = passenger_name
        self.location = location

    def __str__(self):
        return f'({self.passenger_name}, {self.location})'

    # Method to update passenger location
    def move_to(self, new_x, new_y):
        self.location = Location(new_x, new_y)

# RideSharingApp class to manage cars and passengers
class RideSharingApp():
    def __init__(self):
        self.cars = []
        self.passengers = []

    # Add a car to the app
    def add_car(self, car):
        try:
            if not isinstance(car, Car):
                raise TypeError("Only objects of type 'Car' can be added.")
            self.cars.append(car)
        except TypeError as e:
            print(f"Error adding car: {e}")

    # Add a passenger to the app
    def add_passenger(self, passenger):
        try:
            if not isinstance(passenger, Passenger):
                raise TypeError("Only objects of type 'Passenger' can be added.")
            self.passengers.append(passenger)
        except TypeError as e:
            print(f"Error adding passenger: {e}")

    # Remove a car from the app
    def remove_car(self, car):
        try:
            self.cars.remove(car)
        except ValueError as e:
            print(f"Error: {car} not found in the list of cars. {e}")

    # Remove a passenger from the app
    def remove_passenger(self, passenger):
        try:
            self.passengers.remove(passenger)
        except ValueError as e:
            print(f"Error: {passenger} not found in the list of passengers. {e}")

    # Find the cheapest car
    def find_cheapest_car(self):
        try:
            if not self.cars:
                raise ValueError("No cars available.")
            min_cost_per_mile = float('inf')  # Largest possible value to start with
            cheapest_car = None
            for car in self.cars:
                if car.cost_per_mile < min_cost_per_mile:
                    min_cost_per_mile = car.cost_per_mile
                    cheapest_car = car

            if cheapest_car:
                print(f'Cheapest car: {cheapest_car.car_name}, Cost per mile: {cheapest_car.cost_per_mile}')
        except ValueError as e:
            print(f"Error finding the cheapest car: {e}")

    # Find the nearest car to a passenger
    def find_nearest_car(self, passenger):
        try:
            if not isinstance(passenger, Passenger):
                raise TypeError("The argument should be a 'Passenger' object.")
            if not self.cars:
                raise ValueError("No cars available.")
            nearest_car = None
            min_distance = float('inf')  # Largest possible distance to start with
            for car in self.cars:
                distance = math.sqrt((passenger.location.x - car.location.x) ** 2 + (passenger.location.y - car.location.y) ** 2)
                if distance < min_distance:
                    min_distance = distance
                    nearest_car = car

            if nearest_car:
                print(f'Nearest car for {passenger.passenger_name}: {nearest_car.car_name}, Distance: {round(min_distance, 2)}')
        except (TypeError, ValueError) as e:
            print(f"Error finding the nearest car: {e}")

# Main function to test the ride-sharing app
if __name__ == "__main__":
    app = RideSharingApp()

    # Initialize cars and passengers
    car1 = Car("car1", Location(2, 1), 0.61)
    car2 = Car("car2", Location(-4, 1), 0.5)
    passenger1 = Passenger("passenger1", Location(-2, 3))
    passenger2 = Passenger("passenger2", Location(0, 0))

    # Add cars and passengers to the app
    app.add_car(car1)
    app.add_car(car2)
    app.add_passenger(passenger1)
    app.add_passenger(passenger2)

    # Find the cheapest car and the nearest cars to passengers
    app.find_cheapest_car()
    app.find_nearest_car(passenger1)
    app.find_nearest_car(passenger2)
