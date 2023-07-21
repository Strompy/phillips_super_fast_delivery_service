import csv


class DistanceImporter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.addresses = []
        self.distance_lists = []
        self.address_distances = {}

    def parse_file(self):
        reader = csv.reader(open(self.file_path))
        next(reader)
        for row in reader:
            _, address = row[0].splitlines()
            del row[0:2]
            self.addresses.append(address)
            self.distance_lists.append(row)


    def create_address_distances(self):
        for index, address in enumerate(self.addresses):
            distances = []
            for x in range(0, index):
                distances.append(float(self.distance_lists[index][x]))
            for x in range(index, 27):
                distances.append(float(self.distance_lists[x][index]))
            self.address_distances[address] = distances
