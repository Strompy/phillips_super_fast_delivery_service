from datetime import datetime


class Package:
    def __init__(self, package_dict):
        self.id = int(package_dict['id'])
        self.address = package_dict['address']
        self.deadline = package_dict['deadline']
        self.mass = int(package_dict['mass'])
        self.notes = package_dict['notes']
        self.truck_number = None
        self.delivery_time = None

    def delivered_at_time(self):
        if isinstance(self.delivery_time, datetime):
            return self.delivery_time.strftime('%H:%M:%S')
