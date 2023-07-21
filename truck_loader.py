from datetime import datetime, timedelta


class TruckLoader:
    def __init__(self, addresses, address_distances, packages, truck=None, hour=8, minute=0, second=0):
        self.truck = truck
        self.addresses = addresses
        self.address_distances = address_distances
        self.packages = packages
        self.current_datetime = datetime(2023, 7, 21, hour, minute, second)

    def current_time(self):
        return self.current_datetime.strftime('%H:%M:%S')

    def load_truck(self):
        self.truck.add_address_to_route(self.hub())
        while len(self.truck.packages) < 16:
            current_address = self.truck.route[-1]
            current_address_distances = self.address_distances[current_address].copy()
            current_address_distances.sort()
            package_count = len(self.truck.packages)

            for index, distance in enumerate(current_address_distances):
                if distance == 0.0: continue
                address = self.addresses[index]
                for package in self.packages:
                    if self.package_is_valid(package, address):
                        package.truck_number = self.truck.number
                        self.truck.load_package(package)
                        if address in self.truck.route: self.truck.increment_distance(distance)
                        self.truck.add_address_to_route(package.address)
                        minutes_to_destination = self.calculate_time_elapsed(distance)
                        package.delivery_time = self.current_datetime
                        self.increment_current_time(minutes_to_destination)
                        if len(self.truck.packages) >= 16: break
                if len(self.truck.packages) > package_count: break
            if self.all_packages_loaded(): break
        return self.truck

    def package_is_valid(self, package, address):
        if package.truck_number is not None: return False
        if package.address != address: return False
        if package.notes == 'Can only be on truck 2' and self.truck.number != 2: return False
        return True

    def calculate_time_elapsed(self, distance):
        # Calculate time in hours
        time_hours = distance / self.truck_avg_mph()
        # Convert time to minutes
        time_minutes = time_hours * 60 * 60
        return time_minutes

    def truck_avg_mph(self):
        return 18.0

    def increment_current_time(self, seconds):
        # Create a timedelta object representing the time elapsed
        time_elapsed_timedelta = timedelta(seconds=seconds)
        self.current_datetime = self.current_datetime + time_elapsed_timedelta

        # Add the time elapsed to the start time

    # to prioritize packages with deadlines, maybe go through the list of packages and add them to the truck first
    # there is one 9:00AM package and then several 10:30AM packages
    # trucks travel at 18 miles per hour

    def all_packages_loaded(self):
        return len(list(filter(lambda p: p.truck_number is None, self.packages))) == 0

    def hub(self):
        return self.addresses[0]

    # Old route first attempts

    def load_truck_1(self):
        route = [self.hub()]
        truck_1_packages = []
        distance_traveled = 0.0
        while len(truck_1_packages) < 16:
            current_address = route[-1]
            current_address_distances = self.address_distances[current_address].copy()
            current_address_distances.sort()
            package_count = len(truck_1_packages)

            for index, distance in enumerate(current_address_distances):
                if distance == 0.0: continue
                address = self.addresses[index]
                for package in self.packages:
                    if package.address == address and package.truck_number is None:
                        package.truck_number = 1
                        truck_1_packages.append(package)
                        route.append(package.address)
                        distance_traveled += distance
                        if len(truck_1_packages) >= 16: break
                if len(truck_1_packages) > package_count: break
        return route

    def load_truck_2(self):
        route = [self.hub()]
        truck_2_packages = []
        distance_traveled = 0.0
        while len(truck_2_packages) < 16:
            current_address = route[-1]
            current_address_distances = self.address_distances[current_address].copy()
            current_address_distances.sort()
            package_count = len(truck_2_packages)

            for index, distance in enumerate(current_address_distances):
                if distance == 0.0: continue
                address = self.addresses[index]
                for package in self.packages:
                    if package.address == address and package.truck_number is None:
                        package.truck_number = 2
                        truck_2_packages.append(package)
                        route.append(package.address)
                        distance_traveled += distance
                        # break
                        if len(truck_2_packages) >= 16: break
                if len(truck_2_packages) > package_count: break
        return route

    def load_truck_3(self):
        route = [self.hub()]
        truck_3_packages = []
        distance_traveled = 0.0
        while len(truck_3_packages) < 16:
            current_address = route[-1]
            current_address_distances = self.address_distances[current_address].copy()
            current_address_distances.sort()
            package_count = len(truck_3_packages)

            for index, distance in enumerate(current_address_distances):
                if distance == 0.0: continue
                address = self.addresses[index]
                for package in self.packages:
                    if package.address == address and package.truck_number is None:
                        package.truck_number = 3
                        truck_3_packages.append(package)
                        route.append(package.address)
                        distance_traveled += distance
                        unloaded_packages = list(filter(lambda p: p.truck_number == None, self.packages))
                        if len(unloaded_packages) == 0: break
                if len(truck_3_packages) > package_count: break
            if len(list(filter(lambda p: p.truck_number == None, self.packages))) == 0: break
        return route
