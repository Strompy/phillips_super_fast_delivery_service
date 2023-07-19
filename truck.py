class Truck:
    def __init__(self, number):
        self.number = number
        self.packages = []
        self.distance_traveled = 0.0
        self.route = []

    def load_package(self, package):
        self.packages.append(package)
        return self.packages

    def increment_distance(self, distance):
        self.distance_traveled += distance
        return self.distance_traveled

    def add_address_to_route(self, address):
        self.route.append(address)
        return self.route
