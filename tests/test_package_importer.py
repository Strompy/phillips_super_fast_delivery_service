import pytest

from package_importer import PackageImporter

# @pytest.fixture
# def test_importer():
#     return PackageImporter('./docs/packages.csv')

def test_init():
    test_importer = PackageImporter('../docs/packages.csv')
    assert test_importer.file_path == '../docs/packages.csv'
    assert test_importer.package_arrays == []

def test_read_file():
    test_importer = PackageImporter('../docs/packages.csv')
    test_importer.read_file()
    assert len(test_importer.package_arrays) == 40
