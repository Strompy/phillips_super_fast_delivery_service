import csv


class DistanceImporter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.addresses = []
        self.distance_lists = []

    def parse_file(self):
        reader = csv.reader(open(self.file_path))
        next(reader)
        for row in reader:
            _, address = row[0].splitlines()
            distances = row
            del distances[0:2]
            self.addresses.append(address)
            self.distance_lists.append(row)
