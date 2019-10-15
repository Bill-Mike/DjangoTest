# -#- coding:utf-8 -#-
class Director(object):
    def __init__(self):
        self.builder = None

    def construct_building(self):

        self.builder.new_building()
        self.builder.new_building()
        self.builder.new_building()

    def get_building(self):
        return self.builder.building

# Abstract builder
class Builder(object):

    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()

# concrete builder
class BuiderHuose(Builder):
    def buid_floor(self):
        self.building.floor = "ONE"
    def buid_size(self):
        self.building.size = "Big"

class BuilderFlat(Builder):
    def build_floor(self):
        self.building.floor = "More than One"

    def build_size(self):
        self.building.size = "Small"

# Product
class Building(object):
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return "Floor: %s | Size: %s" % (self.floor, self.size)

# Client
if __name__ == "__main__":
    director = Director()
    director.builder = BuiderHuose()
    director.construct_building()
    building = director.get_building()
    print(building)
    director.builder = BuilderFlat()
    director.construct_building()
    building = director.get_building()
    print(building)