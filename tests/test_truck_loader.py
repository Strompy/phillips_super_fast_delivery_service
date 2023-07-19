from distance_importer import DistanceImporter
from package_importer import PackageImporter
from truck import Truck
from truck_loader import TruckLoader


def test_load_truck_1():
    package_importer = PackageImporter('../docs/packages.csv')
    package_importer.parse_file()
    packages = package_importer.create_packages()
    distance_importer = DistanceImporter('../docs/distances.csv')
    distance_importer.parse_file()
    distance_importer.create_address_distances()
    test_truck_loader = TruckLoader(distance_importer.addresses, distance_importer.address_distances, packages)
    route = test_truck_loader.load_truck_1()
    assert route[0] == hub()
    assert len(route) == 17  # this works since there are duplicate addresses
    truck_1_packages = list(filter(lambda p: p.truck_number == 1, packages))
    assert len(truck_1_packages) == 16


def test_load_truck_2():
    package_importer = PackageImporter('../docs/packages.csv')
    package_importer.parse_file()
    packages = package_importer.create_packages()
    distance_importer = DistanceImporter('../docs/distances.csv')
    distance_importer.parse_file()
    distance_importer.create_address_distances()
    test_truck_loader = TruckLoader(distance_importer.addresses, distance_importer.address_distances, packages)
    route = test_truck_loader.load_truck_2()
    assert route[0] == hub()
    assert len(route) == 17
    truck_2_packages = list(filter(lambda p: p.truck_number == 2, packages))
    assert len(truck_2_packages) == 16


def test_load_truck_3():
    package_importer = PackageImporter('../docs/packages.csv')
    package_importer.parse_file()
    packages = package_importer.create_packages()
    distance_importer = DistanceImporter('../docs/distances.csv')
    distance_importer.parse_file()
    distance_importer.create_address_distances()
    test_truck_loader = TruckLoader(distance_importer.addresses, distance_importer.address_distances, packages)
    route = test_truck_loader.load_truck_3()
    assert route[0] == hub()
    assert len(route) == 18
    truck_3_packages = list(filter(lambda p: p.truck_number == 3, packages))
    assert len(truck_3_packages) == 17


def test_load_trucks_1_and_2_and_3():
    package_importer = PackageImporter('../docs/packages.csv')
    package_importer.parse_file()
    packages = package_importer.create_packages()
    distance_importer = DistanceImporter('../docs/distances.csv')
    distance_importer.parse_file()
    distance_importer.create_address_distances()
    test_truck_loader = TruckLoader(distance_importer.addresses, distance_importer.address_distances, packages)
    route = test_truck_loader.load_truck_1()
    assert route[0] == hub()
    assert len(route) == 17  # this works since there are duplicate addresses
    truck_1_packages = list(filter(lambda p: p.truck_number == 1, packages))
    assert len(truck_1_packages) == 16

    route_2 = test_truck_loader.load_truck_2()
    assert route_2[0] == hub()
    assert len(route_2) == 17
    truck_2_packages = list(filter(lambda p: p.truck_number == 2, packages))
    assert len(truck_2_packages) == 16

    route_3 = test_truck_loader.load_truck_3()
    assert route_3[0] == hub()
    assert len(route_3) == 9
    truck_3_packages = list(filter(lambda p: p.truck_number == 3, packages))
    assert len(truck_3_packages) == 8


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
    assert len(truck_1.route) == 17  # this works since there are duplicate addresses
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
    assert len(truck_1.route) == 17  # this works since there are duplicate addresses
    truck_1_packages = list(filter(lambda p: p.truck_number == 1, packages))
    assert len(truck_1_packages) == 16
    assert len(truck_1.packages) == 16
    assert truck_1.distance_traveled != 0.0

    truck_2 = Truck(2)
    truck_loader = TruckLoader(distance_importer.addresses, distance_importer.address_distances, unloaded_packages,
                               truck_2)
    truck_loader.load_truck()
    assert truck_2.route[0] == hub()
    assert len(truck_2.route) == 17  # this works since there are duplicate addresses
    truck_2_packages = list(filter(lambda p: p.truck_number == 2, packages))
    assert len(truck_2_packages) == 16
    assert len(truck_2.packages) == 16
    assert truck_2.distance_traveled != 0.0

    truck_3 = Truck(3)
    # unloaded_packages = unloaded_packages()
    truck_loader = TruckLoader(distance_importer.addresses, distance_importer.address_distances, unloaded_packages,
                               truck_3)
    truck_loader.load_truck()
    assert truck_3.route[0] == hub()
    assert len(truck_3.route) == 17  # this works since there are duplicate addresses
    truck_3_packages = list(filter(lambda p: p.truck_number == 3, packages))
    assert len(truck_3_packages) == 16
    assert len(truck_3.packages) == 16
    assert truck_3.distance_traveled != 0.0


def unloaded_packages():
    return list(filter(lambda p: p.truck_number == None, packages))


def hub():
    return '1644 Platte St, Denver, CO 80202'
