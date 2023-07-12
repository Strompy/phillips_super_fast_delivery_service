from distance_importer import DistanceImporter


def test_distance_importer_init():
    test_importer = DistanceImporter('../docs/distances.csv')
    assert test_importer.file_path == '../docs/distances.csv'
    assert test_importer.addresses == []
    assert test_importer.distance_lists == []


def test_parse_file():
    test_importer = DistanceImporter('../docs/distances.csv')
    test_importer.parse_file()
    assert len(test_importer.addresses) == 27
    assert len(test_importer.distance_lists) == 27
    for distances in test_importer.distance_lists:
        assert len(distances) == 27
