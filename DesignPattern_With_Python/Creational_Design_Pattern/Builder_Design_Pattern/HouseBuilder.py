from IHouseBuilder import IHouseBuilder
from House import House


class HouseBuilder(IHouseBuilder):
    """ The concrete builder"""

    def __init__(self):
        self.house = House()

    def set_wall_material(self, value):
        self.house.wall_materials = value
        return self

    def set_building_type(self, value):
        self.house.building_type = value
        return self

    def set_number_doors(self, value):
        self.house.doors = value
        return self

    def set_number_windows(self, value):
        self.house.windows = value
        return self

    def get_result(self):
        return self.house
