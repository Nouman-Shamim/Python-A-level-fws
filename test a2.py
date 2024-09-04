class ParkingArea:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = min(capacity, 300)
        self.vehicles = [None] * self.capacity

    def get_name(self):
        return self.name

    def get_capacity(self):
        return self.capacity

    def find_vehicle(self, reg):
        # find where the vehicle is located in the list and
        # return the index not yet written
        pass

class Vehicle:
    BLACK = 1
    WHITE = 2
    BLUE = 3
    RED = 4
    GREEN = 5
    ADMIN_FEE = 3.0

    def __init__(self, registration=None, colour=None):
        self.registration = registration
        self.colour = colour
        self.broken = False

    def set_broken(self, broken):
        self.broken = broken

    def set_colour(self, colour):
        self.colour = colour

    def get_broken(self):
        return self.broken

    def get_registration(self):
        return self.registration

    def pay(self, hours):
        # code to return admin fee - only if applicable
        pass


