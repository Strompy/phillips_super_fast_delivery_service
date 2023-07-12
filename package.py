class Package:
    def __init__(self, package_dict):
        self.id = int(package_dict['id'])
        self.address = package_dict['address']
        self.delivery_time = package_dict['deadline']
        self.mass = int(package_dict['mass'])
        self.notes = package_dict['notes']
