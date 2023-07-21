from datetime import datetime, timedelta, time


class TruckLoader:
    def __init__(self, addresses, address_distances, packages, truck=None, hour=8, minute=0, second=0):
        self.truck = truck
        self.addresses = addresses
        self.address_distances = address_distances
        self.packages = packages
        self.current_datetime = datetime.combine(datetime.today(),
                                                 time(8, 0))  # datetime(2023, 7, 21, hour, minute, second)

    def current_time(self):
        return self.current_datetime.strftime('%H:%M:%S')

    def load_truck_unoptimized(self):
        self.truck.add_address_to_route(self.hub())
        while len(self.truck.packages) < 16:
            current_address = self.truck.route[-1]
            current_address_distances = self.address_distances[current_address].copy()
            current_address_distances.sort()
            package_count = len(self.truck.packages)

            for index, distance in enumerate(current_address_distances):
                if distance == 0.0: continue
                address = self.addresses[index]  # this index doesn't match anymore since it was sorted
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

    def load_truck(self):
        self.truck.add_address_to_route(self.hub())
        invalid_distances = [0.0]

        while len(self.truck.packages) < 16:
            current_address = self.truck.route[-1]
            current_address_distances = self.address_distances[current_address].copy()
            package_count = len(self.truck.packages)
            smallest_distance_indices = self.get_indices_of_smallest_valid_distance(current_address_distances,
                                                                                    invalid_distances)
            for index in smallest_distance_indices:
                distance = current_address_distances[index]
                address = self.addresses[index]
                if address == self.hub(): continue
                for package in self.packages:
                    if self.package_is_valid(package, address):
                        package.truck_number = self.truck.number
                        self.truck.load_package(package)
                        if self.truck.route[-1] != address:
                            self.truck.increment_distance(distance)
                            seconds_to_destination = self.calculate_time_elapsed(distance)
                            self.increment_current_time(seconds_to_destination)

                        # at the moment I am adding duplicate addresses to the route
                        self.truck.add_address_to_route(package.address)
                        package.delivery_time = self.current_datetime
                        if len(self.truck.packages) >= 16: break

                    # if I added packages I have completed a stop and need to start again from the new current address
                    if len(self.truck.packages) > package_count:
                        invalid_distances = [0.0]
                        break

            # if no packages were added to the truck for any indices
            # then I need to add the distance to the invalid distances
            if len(self.truck.packages) == package_count: invalid_distances.append(distance)

            if self.all_packages_loaded(): break
        return self.truck

    def get_indices_of_smallest_valid_distance(self, current_address_distances, invalid_distances):
        # Filter out elements that are not in custom_list
        valid_distances = [distance for distance in current_address_distances if distance not in invalid_distances]

        if not valid_distances:
            "The list does not contain any valid distances elements."
            # this is hitting when I have one package remaining, '2056 Newton St, Denver, CO 80211'
            # Unless I load truck 2 first, I need to prioritize loading of Truck 2 based on the package notes
            raise ValueError

        # Find the minimum distance among non-zero elements
        min_distance = min(valid_distances)

        # Find all indices of the minimum distance in the original list
        min_indices = [index for index, distance in enumerate(current_address_distances) if distance == min_distance]

        return min_indices
        # This will get me the indices of the smallest distances in the list
        # I would like to add to the invalid distances once I have confirmed the packages
        # for that address if packages are loaded or requirements are unmet
        # I return the multiple indices to ensure that I can check all addresses with the same distance

    def package_is_valid(self, package, address):
        if package.truck_number is not None: return False
        if package.address != address: return False
        if package.notes == 'Can only be on truck 2' and self.truck.number != 2: return False
        return True

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

    # to prioritize packages with deadlines, maybe go through the list of packages and add them to the truck first
    # there is one 9:00AM package and then several 10:30AM packages
    # trucks travel at 18 miles per hour

    def all_packages_loaded(self):
        return len(list(filter(lambda p: p.truck_number is None, self.packages))) == 0

    def hub(self):
        return self.addresses[0]
