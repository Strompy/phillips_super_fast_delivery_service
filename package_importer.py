import csv
class PackageImporter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.package_arrays = []
        self.packages = []

    def read_file(self):
        reader = csv.DictReader(open(self.file_path))
        for row in reader:
            print(row)
            self.package_arrays.append(row)
