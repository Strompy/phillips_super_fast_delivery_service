from distance_importer import DistanceImporter

def test_distance_importer_init():
    test_importer = DistanceImporter('../docs/distances.csv')
    assert test_importer.file_path == '../docs/distances.csv'
    assert test_importer.addresses == []
    assert test_importer.distance_lists == []


