from distance_importer import DistanceImporter

def test_everything():
    test_distance_importer_init()
    test_parse_file()
    test_create_address_distances()

def test_distance_importer_init():
    test_importer = DistanceImporter('../docs/distances.csv')
    assert test_importer.file_path == '../docs/distances.csv'
    assert test_importer.addresses == []
    assert test_importer.distance_lists == []
    assert test_importer.address_distances == {}


def test_parse_file():
    test_importer = DistanceImporter('../docs/distances.csv')
    test_importer.parse_file()
    assert len(test_importer.addresses) == 27
    assert len(test_importer.distance_lists) == 27
    for distances in test_importer.distance_lists:
        assert len(distances) == 27

def test_create_address_distances():
    test_importer = DistanceImporter('../docs/distances.csv')
    test_importer.parse_file()
    test_importer.create_address_distances()
    assert len(test_importer.address_distances) == 27
    for address, distances in test_importer.address_distances.items():
        assert len(distances) == 27
        list(filter(('').__ne__, distances)) # removes any blank string entries from the original dataset
        length = len(list(filter(('').__ne__, distances)))
        assert length == 27
        # the index of the address should return of distance of 0.0, the distance between its own address
        address_index = test_importer.addresses.index(address)
        assert distances[address_index] == 0.0
