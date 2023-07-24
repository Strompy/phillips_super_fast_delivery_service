from datetime import datetime, time

from distance_importer import DistanceImporter
from package_importer import PackageImporter
from truck import Truck
from truck_loader import TruckLoader


def test_truck_loader_init():
    distance_importer = DistanceImporter('../docs/distances.csv')
    distance_importer.parse_file()
    distance_importer.create_address_distances()
    package_importer = PackageImporter('../docs/packages.csv')
    package_importer.parse_file()
    packages = package_importer.create_packages()
    truck_1 = Truck(1)
    truck_loader = TruckLoader(distance_importer.addresses, distance_importer.address_distances, packages, truck_1)
    assert truck_loader.addresses == distance_importer.addresses
    assert truck_loader.address_distances == distance_importer.address_distances
    assert truck_loader.packages == packages
    assert truck_loader.truck == truck_1
    assert truck_loader.current_time() == '08:00:00'


def test_load_truck():
    package_importer = PackageImporter('../docs/packages.csv')
    package_importer.parse_file()
    packages = package_importer.create_packages()
    distance_importer = DistanceImporter('../docs/distances.csv')
    distance_importer.parse_file()
    distance_importer.create_address_distances()
    truck_1 = Truck(1)
    truck_loader = TruckLoader(distance_importer.addresses, distance_importer.address_distances, packages, truck_1)
    truck_loader.load_truck()
    assert truck_1.route[0] == hub()
    assert len(truck_1.route) == 17  # addresses are added for each package
    truck_1_packages = list(filter(lambda p: p.truck_number == 1, packages))
    assert len(truck_1_packages) == 16
    assert len(truck_1.packages) == 16
    assert truck_1.distance_traveled != 0.0


def test_load_all_trucks():
    package_importer = PackageImporter('../docs/packages.csv')
    package_importer.parse_file()
    packages = package_importer.create_packages()
    distance_importer = DistanceImporter('../docs/distances.csv')
    distance_importer.parse_file()
    distance_importer.create_address_distances()
    truck_1 = Truck(1)
    truck_loader = TruckLoader(distance_importer.addresses, distance_importer.address_distances, packages, truck_1)
    truck_loader.load_truck()
    assert truck_1.route[0] == hub()
    assert len(truck_1.route) == 17
    truck_1_packages = filter_packages(packages, 1)
    assert len(truck_1_packages) == 16
    assert len(truck_1.packages) == 16
    assert truck_1.distance_traveled > 0.0
    assert truck_loader.current_time() != '08:00:00'
    # load truck 2
    truck_2 = Truck(2)
    unloaded = filter_packages(packages)
    truck_loader = TruckLoader(distance_importer.addresses, distance_importer.address_distances, unloaded, truck_2)
    truck_loader.load_truck_2()
    assert truck_2.route[0] == hub()
    assert len(truck_2.route) == 17
    required_truck_2_packages = [package for package in packages if package.notes == 'Can only be on truck 2']
    for package in required_truck_2_packages:
        assert package.truck_number == 2
    truck_2_packages = filter_packages(packages, 2)
    assert len(truck_2_packages) == 16
    assert len(truck_2.packages) == 16
    assert truck_2.distance_traveled > 0.0
    # load truck 3
    truck_3 = Truck(3)
    unloaded = filter_packages(packages)
    truck_loader = TruckLoader(distance_importer.addresses, distance_importer.address_distances, unloaded, truck_3, 9, 5, 0)
    truck_loader.load_truck()
    assert truck_3.route[0] == hub()
    assert len(truck_3.route) == 9
    truck_3_packages = filter_packages(packages, 3)
    assert len(truck_3_packages) == 8
    assert truck_3.distance_traveled > 0.0
    total_distance = truck_1.distance_traveled + truck_2.distance_traveled + truck_3.distance_traveled
    assert total_distance < 140.0
    for package in packages:
        assert package.delivered_at_time() is not None

def test_load_truck_with_deadlines():
    package_importer = PackageImporter('../docs/packages.csv')
    package_importer.parse_file()
    packages = package_importer.create_packages()
    distance_importer = DistanceImporter('../docs/distances.csv')
    distance_importer.parse_file()
    distance_importer.create_address_distances()
    truck_1 = Truck(1)
    truck_loader_1 = TruckLoader(distance_importer.addresses, distance_importer.address_distances, packages, truck_1)
    truck_loader_1.load_truck()
    truck_2 = Truck(2)
    truck_loader_2 = TruckLoader(distance_importer.addresses, distance_importer.address_distances, packages, truck_2)
    truck_loader_2.load_truck_2()
    truck_3 = Truck(3)
    truck_loader_3 = TruckLoader(distance_importer.addresses, distance_importer.address_distances, packages, truck_3)
    truck_loader_3.load_truck()
    nine_am_packages = list(filter(lambda p: p.deadline == '9:00 AM', packages))
    ten_thirty_am_packages = list(filter(lambda p: p.deadline == '10:30 AM', packages))
    for package in nine_am_packages:
        assert package.delivery_time <= datetime.combine(datetime.today(), time(9, 0))

    for package in ten_thirty_am_packages:
        assert package.delivery_time <= datetime.combine(datetime.today(), time(10, 30))


def hub():
    return '1644 Platte St, Denver, CO 80202'


def filter_packages(packages, number=None):
    return list(filter(lambda p: p.truck_number == number, packages))
