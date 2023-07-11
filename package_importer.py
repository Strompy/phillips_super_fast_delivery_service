import csv
class PackageImporter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.packages = {}

    def read_file(self):
        with open(self.file_path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(', '.join(row))
