import csv

from package import Package


class PackageImporter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.package_dicts = []
        self.packages = []

    def read_file(self):
        reader = csv.DictReader(open(self.file_path))
        for row in reader:
            # print(row)
            self.package_dicts.append(row)

    def create_packages(self):
        for p in self.package_dicts:
            p['address'] = self.build_address(p)
            print(p)
            package = Package(p)
            self.packages.append(package)

    def build_address(self, package_dict):
        street = package_dict['address']
        city = package_dict['city']
        state = package_dict['state']
        zip = package_dict['zip']
        address = ', '.join([street, city, state])
        address = address + ' ' + zip
        print(address)
        return address
