from package import Package
from truck import Truck


def test_truck_init():
    test_truck = Truck(1)
    assert test_truck.number == 1
    assert test_truck.packages == []
    assert test_truck.distance_traveled == 0.0
    assert test_truck.route == []

def test_load_package():
    test_truck = Truck(1)
    test_package = Package({'id': '3',
                            'address': '5430 Zuni St, Denver, CO 80221',
                            'deadline': 'EOD',
                            'mass': '2',
                            'notes': 'Can only be on truck 2'})
    test_truck.load_package(test_package)
    assert test_truck.packages == [test_package]
    assert test_truck.load_package(test_package) == [test_package, test_package]

def test_increment_distance():
    test_truck = Truck(1)
    test_truck.increment_distance(10.0)
    assert test_truck.distance_traveled == 10.0
    test_truck.increment_distance(5.0)
    assert test_truck.distance_traveled == 15.0

def test_add_address_to_route():
    test_truck = Truck(1)
    test_truck.add_address_to_route('1644 Platte St, Denver, CO 80202')
    assert test_truck.route == ['1644 Platte St, Denver, CO 80202']
    test_truck.add_address_to_route('5430 Zuni St, Denver, CO 80221')
    assert test_truck.route == ['1644 Platte St, Denver, CO 80202', '5430 Zuni St, Denver, CO 80221']