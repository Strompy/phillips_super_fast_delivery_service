import csv

class DistanceImporter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.addresses = []
        self.distance_lists = []

