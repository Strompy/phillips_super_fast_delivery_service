from datetime import datetime, timedelta, time


class TruckLoader:
    def __init__(self, addresses, address_distances, packages, truck=None, time='08:00:00'):
        self.truck = truck
        self.addresses = addresses
        self.address_distances = address_distances
        self.packages = packages
        self.current_datetime = datetime.combine(datetime.today(), self.parse_time(time))
        self.address_needs_updating = True

    def parse_time(self, string):
        return datetime.strptime(string, '%H:%M:%S').time()

    def current_time(self):
        return self.current_datetime.strftime('%H:%M:%S')

    def load_truck(self):
        if len(self.truck.route) == 0:
            self.truck.add_address_to_route(self.hub())
        current_address = ''
        while len(self.truck.packages) < 16:
            if current_address != self.last_route_address():
                invalid_distances = [0.0]
            current_address = self.last_route_address()
            current_address_distances = self.address_distances[current_address].copy()
            package_count = len(self.truck.packages)
            smallest_distance_indices = self.get_indices_of_smallest_valid_distance(current_address_distances, invalid_distances)
            if smallest_distance_indices is None: break
            for index in smallest_distance_indices:
                distance = current_address_distances[index]
                address = self.addresses[index]
                packages_at_address = [package for package in self.packages if package.address == address]
                if not self.room_on_truck(packages_at_address): continue
                self.validate_and_load_packages(packages_at_address, address, distance)
            # if no packages were added to the truck then distance in invalid
            if len(self.truck.packages) == package_count:
                invalid_distances.append(distance)
            if self.all_packages_loaded(): break
        return self.truck

    def get_indices_of_smallest_valid_distance(self, current_address_distances, invalid_distances):
        valid_distances = [distance for distance in current_address_distances if distance not in invalid_distances]
        if not valid_distances:
            # raise ValueError("The list does not contain any valid distances elements.")
            return None
        min_distance = min(valid_distances)
        min_indices = [index for index, distance in enumerate(current_address_distances) if distance == min_distance]
        # return multiple indices to ensure that I can check all addresses with the same distance
        return min_indices

    def room_on_truck(self, packages_at_address=[]):
        # if self.truck.number == 2:
        #     return len(self.truck.packages) + len(packages_at_address) <= 15
        # else:
            return len(self.truck.packages) + len(packages_at_address) <= 16

    def package_is_valid(self, package, address):
        if package.truck_number is not None: return False
        if package.address != address: return False
        if package.notes == 'Can only be on truck 2' and self.truck.number != 2: return False
        if package.notes == 'Delayed on flight---will not arrive to depot until 9:05 am' and self.truck.number != 3: return False
        # if package.notes == 'Wrong address listed' and not self.updated_address_available(): return False
        return True

    # def updated_address_available(self):
        # return self.current_datetime >= datetime.combine(datetime.today(), time(10, 20))

    def validate_and_load_packages(self, packages_at_address, address, distance):
        # check all packages_at_address are valid
        result = self.check_list_of_packages(packages_at_address, address)
        if result:
            self.load_packages(packages_at_address, address, distance)

    def check_list_of_packages(self, packages_at_address, address):
        for package in packages_at_address:
            if not self.package_is_valid(package, address):
                return False
        return True

    def load_packages(self, packages_at_address, address, distance):
        # then load all packages_at_address if valid
        for package in packages_at_address:
            # if self.package_is_valid(package, address):
            package.truck_number = self.truck.number
            self.truck.load_package(package)
            if self.last_route_address() != address:
                self.truck.increment_distance(distance)
                seconds_to_destination = self.calculate_time_elapsed(distance)
                self.increment_current_time(seconds_to_destination)
            self.truck.add_address_to_route(package.address)
            package.delivery_time = self.current_datetime
                # if self.address_needs_updating and self.updated_address_available(): self.update_wrong_address()

    # def update_wrong_address(self):
    #     package = next(package for package in self.packages if package.notes == 'Wrong address listed')
    #     self.address_needs_updating = False
    #     package.update_address('5100 Zuni St, Denver, CO 80221')
    #     return package

    def calculate_time_elapsed(self, distance):
        time_hours = distance / self.truck_avg_mph()
        time_seconds = time_hours * 60 * 60
        return time_seconds

    @staticmethod
    def truck_avg_mph():
        return 18.0

    def increment_current_time(self, seconds):
        time_elapsed_timedelta = timedelta(seconds=seconds)
        self.current_datetime = self.current_datetime + time_elapsed_timedelta

    def all_packages_loaded(self):
        return len(list(filter(lambda p: p.truck_number is None, self.packages))) == 0

    def last_route_address(self):
        return self.truck.route[-1]

    def hub(self):
        return self.addresses[0]

    def load_truck_1(self):
        self.load_truck()
        # truck_1 returns to hub after loading to get driver onto truck 3
        distance = self.address_distances[self.last_route_address()][0]
        self.truck.add_address_to_route(self.hub())
        self.truck.increment_distance(distance)
        seconds_to_destination = self.calculate_time_elapsed(distance)
        self.increment_current_time(seconds_to_destination)
        return self.truck


    def load_truck_3(self):
        self.truck.add_address_to_route(self.hub())
        current_address = self.last_route_address()
        current_address_distances = self.address_distances[current_address].copy()
        farthest_required_address = '4101 Inca St, Denver, CO 80211'
        index = self.addresses.index(farthest_required_address)
        distance = current_address_distances[index]
        address = self.addresses[index]
        packages_at_address = [package for package in self.packages if package.address == address]
        self.validate_and_load_packages(packages_at_address, address, distance)

        self.load_truck()
        return self.truck


    def load_truck_2(self):
        self.truck.add_address_to_route(self.hub())
        current_address = self.last_route_address()
        current_address_distances = self.address_distances[current_address].copy()
        farthest_required_address = '2056 Newton St, Denver, CO 80211'
        index = self.addresses.index(farthest_required_address)
        distance = current_address_distances[index]
        address = self.addresses[index]
        packages_at_address = [package for package in self.packages if package.address == address]
        self.validate_and_load_packages(packages_at_address, address, distance)

        self.load_truck()

        # self.truck.packages
        # self.wait_until_updated_address_time()
        # package = self.update_wrong_address()
        # current_address = self.last_route_address()
        # current_address_distances = self.address_distances[current_address].copy()
        # index = self.addresses.index(package.address)
        # distance = current_address_distances[index]
        # address = self.addresses[index]
        # self.validate_and_load_packages([package], address, distance)

    def wait_until_updated_address_time(self):
        # if time is earlier than 10:20am, set time to 10:20am
        if self.current_datetime.time() < time(10, 20):
            self.current_datetime = datetime.combine(datetime.today(), time(10, 20))