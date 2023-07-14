from package import Package

from package_importer import PackageImporter

def test_init():
    test_importer = PackageImporter('../docs/packages.csv')
    assert test_importer.file_path == '../docs/packages.csv'
    assert test_importer.package_dicts == []

def test_read_file():
    test_importer = PackageImporter('../docs/packages.csv')
    test_importer.parse_file()
    assert len(test_importer.package_dicts) == 40

def test_build_address():
    test_importer = PackageImporter('../docs/packages.csv')
    package_dict = {'id': '3', 'address': '5430 Zuni St', 'city': 'Denver', 'state': 'CO', 'zip': '80221', 'deadline': 'EOD', 'mass': '2', 'notes': 'Can only be on truck 2'}
    assert test_importer.build_address(package_dict) == '5430 Zuni St, Denver, CO 80221'

def test_create_packages():
    test_importer = PackageImporter('../docs/packages.csv')
    test_importer.parse_file()
    test_importer.create_packages()
    assert len(test_importer.packages) == 40
    for p in test_importer.packages:
        assert isinstance(p, Package)
