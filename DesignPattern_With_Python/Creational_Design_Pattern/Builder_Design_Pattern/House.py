
class House():

    """ The product"""

    def __init__(self,building_type ="Apartment", doors =0,windows=0, wall_materials ="bricks"):
        #brick, wood, straw, ice
        self.wall_materials = wall_materials
        self.building_type =  building_type
        self.doors = doors
        self.windows = windows

    def __str__(self):
        return "This is a {0}{1} with {2} door(s) and {3} window(s).".format(
            self.wall_materials,self.building_type, self.doors,self.windows
        )


