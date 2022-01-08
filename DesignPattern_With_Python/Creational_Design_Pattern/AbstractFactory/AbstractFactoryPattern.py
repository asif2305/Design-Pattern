from abc import ABCMeta, abstractstaticmethod
from chair_factory import ChairFactory
from table_factory import TableFactory

"""
The Abstract Factory Pattern adds an abstract layer over multiple factory method implementations
The Abstract Factory contains or composites one or more than one factory method

"""

class IFurnitureFacotry(metaclass=ABCMeta):
    @staticmethod
    def get_furniture(furniture_type):
        """ The static furniture factory interfaces method """


class FurnitureFactory(IFurnitureFacotry):

    @staticmethod
    def get_furniture(furniture_type):
        try:
            if furniture_type in ["BigChair", "MediumChair", "SmallChair"]:
                return ChairFactory.get_chair_type(furniture_type)
            if furniture_type in ["BigTable", "MediumTable", "SmallTable"]:
                return TableFactory.get_table_type(furniture_type)
            raise AssertionError("Cannot find furniture type")
        except AssertionError as _e:
            print(_e)
        return None

if __name__ == "__main__" :
    furniture_factory = FurnitureFactory.get_furniture("SmallChair")
    print(f"{furniture_factory.__class__} : {furniture_factory.get_dimensions()}")

    furniture_factory = FurnitureFactory.get_furniture("BigTable")
    print(f"{furniture_factory.__class__} : {furniture_factory.get_dimensions()}")