from HouseBuilder import HouseBuilder

class HouseBoatDirector():
    """The Director, building a different representaions"""

    @staticmethod
    def construct():
        return HouseBuilder()\
               .set_building_type("House Boat")\
               .set_wall_material("Wooden")\
               .set_number_doors(6)\
               .set_number_windows(8)\
               .get_result()

class IglooDirector():
    """The Director, building a different representaions"""

    @staticmethod
    def construct():
        return HouseBuilder()\
               .set_building_type("Igloo")\
               .set_wall_material("Ice")\
               .set_number_doors(1)\
               .set_number_windows(0)\
               .get_result()

class CastleDirector():
    """The Director, building a different representaions"""

    @staticmethod
    def construct():
        return HouseBuilder()\
               .set_building_type("Castle")\
               .set_wall_material("Granite")\
               .set_number_doors(100)\
               .set_number_windows(200).get_result()

if __name__ =="__main__":
    Igloo = IglooDirector.construct()
    print(Igloo)
    house = HouseBoatDirector.construct()
    print(house)
    castle = CastleDirector.construct()
    print(castle)


