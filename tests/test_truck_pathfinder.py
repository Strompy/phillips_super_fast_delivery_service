from distance_importer import DistanceImporter
from package_importer import PackageImporter
from truck_pathfinder import TruckPathfinder

def test_load_truck_1():
    package_importer = PackageImporter('../docs/packages.csv')
    package_importer.parse_file()
    packages = package_importer.create_packages()
    distance_importer = DistanceImporter('../docs/distances.csv')
    distance_importer.parse_file()
    distance_importer.create_address_distances()
    test_truck_pathfinder = TruckPathfinder(distance_importer.addresses, distance_importer.address_distances, packages)
    route = test_truck_pathfinder.load_truck_1()
    assert len(route) == 17
    assert route[0] == hub()
    assert len(route) == len(set(route))
    truck_1_packages = list(filter(lambda p: p.truck_number == 1, packages))
    assert len(truck_1_packages) == 16

def test_load_truck_2():
    package_importer = PackageImporter('../docs/packages.csv')
    package_importer.parse_file()
    packages = package_importer.create_packages()
    distance_importer = DistanceImporter('../docs/distances.csv')
    distance_importer.parse_file()
    distance_importer.create_address_distances()
    test_truck_pathfinder = TruckPathfinder(distance_importer.addresses, distance_importer.address_distances, packages)
    route = test_truck_pathfinder.load_truck_2()
    assert len(route) == 17
    assert route[0] == hub()
    assert len(route) == len(set(route))
    truck_2_packages = list(filter(lambda p: p.truck_number == 2, packages))
    assert len(truck_2_packages) == 16

def test_load_trucks_1_and_2():
    package_importer = PackageImporter('../docs/packages.csv')
    package_importer.parse_file()
    packages = package_importer.create_packages()
    distance_importer = DistanceImporter('../docs/distances.csv')
    distance_importer.parse_file()
    distance_importer.create_address_distances()
    test_truck_pathfinder = TruckPathfinder(distance_importer.addresses, distance_importer.address_distances, packages)
    route_1 = test_truck_pathfinder.load_truck_1()
    route_2 = test_truck_pathfinder.load_truck_2(route_1)
    assert len(route_1) == 17
    # the route length doesn't matter so much. It's package count and multiple packages can go to one address
    assert route_1[0] == hub()
    assert len(route_1) == len(set(route_1))
    truck_1_packages = list(filter(lambda p: p.truck_number == 1, packages))
    assert len(truck_1_packages) == 16

    # assert len(route_2) == 17
    # assert route_2[0] == hub()
    # assert len(route_2) == len(set(route_2))
    # truck_2_packages = list(filter(lambda p: p.truck_number == 2, packages))
    # assert len(truck_2_packages) == 16


def hub():
    return '1644 Platte St, Denver, CO 80202'