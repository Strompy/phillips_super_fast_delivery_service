class TruckLoader:
    def __init__(self, addresses, address_distances, packages, truck = None):
        self.truck = truck
        self.addresses = addresses
        self.address_distances = address_distances
        self.packages = packages

    def load_truck(self):
        self.truck.add_address_to_route(self.hub())
        # truck_packages = []
        while len(self.truck.packages) < 16:
            current_address = self.truck.route[-1]
            current_address_distances = self.address_distances[current_address].copy()
            current_address_distances.sort()
            package_count = len(self.truck.packages)

            for index, distance in enumerate(current_address_distances):
                if distance == 0.0: continue
                address = self.addresses[index]
                for package in self.packages:
                    if package.address == address and package.truck_number is None:
                        package.truck_number = self.truck.number
                        self.truck.load_package(package)
                        self.truck.add_address_to_route(package.address)
                        self.truck.increment_distance(distance)
                        if len(self.truck.packages) >= 16: break
                if len(self.truck.packages) > package_count: break
        return self.truck

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

    # def find_closest_package(self, address):

    def hub(self):
        return self.addresses[0]
