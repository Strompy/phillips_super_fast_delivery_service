class TruckPathfinder:
    def __init__(self, addresses, address_distances):
        # self.truck = truck
        # self.warehouse = warehouse
        self.addresses = addresses
        self.address_distances = address_distances

    def find_path_from_hub(self):
        #          start at address[0] (hub)
        #          find the shortest distance in address_distances[address[0]] that isn't '0.0
        #          use the index of that distance to find the address in addresses
        #          add that address to the route
        #          repeat until 16 addresses are in the route
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
                        route.append(address)
                        distance_traveled += distance
                        break

        return route




