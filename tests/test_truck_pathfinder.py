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



def hub():
    return '1644 Platte St, Denver, CO 80202'