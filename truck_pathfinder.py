class TruckPathfinder:
    def __init__(self, addresses, address_distances, packages):
        # self.truck = truck
        # self.warehouse = warehouse
        self.addresses = addresses
        self.address_distances = address_distances
        self.packages = packages

    def load_truck_1(self):
        route = [self.addresses[0]]
        distance_traveled = 0.0
        while len(route) < 17:
            current_address = route[-1]
            current_address_distances = self.address_distances[current_address].copy()
            current_address_distances.sort()

            for distance in current_address_distances:
                if distance != 0.0:
                    index = self.address_distances[current_address].index(distance)
                    address = self.addresses[index]
                    if address not in route:
                        # iterate through packages and find the package with the matching address
                        for package in self.packages:
                            # if address matches and truck isn't full load package on the truck
                            if len(route) >= 17: break
                            if package.address == address and package.truck_number is None:
                                package.truck_number = 1
                                route.append(address)
                                distance_traveled += distance
                                break



        return route




