import datetime

from package import Package


def test_package_init():
    test_package = Package({'id': '3',
                            'address': '5430 Zuni St, Denver, CO 80221',
                            'deadline': 'EOD',
                            'mass': '2',
                            'notes': 'Can only be on truck 2'})
    assert test_package.id == 3
    assert test_package.address == '5430 Zuni St, Denver, CO 80221'
    assert test_package.deadline
    assert test_package.mass == 2
    assert test_package.notes == 'Can only be on truck 2'
    assert test_package.truck_number is None
    assert test_package.delivery_time is None


def test_delivered_at_time():
    test_package = Package({'id': '3',
                            'address': '5430 Zuni St, Denver, CO 80221',
                            'deadline': 'EOD',
                            'mass': '2',
                            'notes': 'Can only be on truck 2'})
    test_package.delivery_time = datetime.datetime(2020, 1, 1, 13, 0, 0)
    assert test_package.delivered_at_time() == '13:00:00'
