# Resource
# https://www.youtube.com/watch?v=04J_fL5zg3U&ab_channel=seanwasereytbe

from abc import ABCMeta, abstractstaticmethod

"""
Factory method is a creational design pattern that provides an interface for creating 
object in a superclass, but allows subclasses to alter the type of object 
that will be created
It is used when we don't know how many or what type of objects will be needed until during runtime
"""


# declare a interface
class IBus(metaclass=ABCMeta):

    macH=10
    startTime =100
    endTime=200

    @staticmethod
    def get_bus_dimensions():
        """ The Bus Interface """


class SchoolBus(IBus):

    def __init__(self):
        self.width = 100
        self.height = 60
        self.color = "Green"

    def get_bus_dimensions(self):

        return {"width": self.width, "height": self.height, "Color": self.color}


class CollegeBus(IBus):

    def __init__(self):
        self.width = 150
        self.height = 70
        self.color = "Blue"

    def get_bus_dimensions(self):
        return {"width": self.width, "height": self.height, "Color": self.color}


class UniversityBus(IBus):

    def __init__(self):
        self.width = 200
        self.height = 100
        self.color = "Red"

    def get_bus_dimensions(self):
        return {"width": self.width, "height": self.height, "Color": self.color}


# now create the Bus Factory class

class BusFactory():

    @staticmethod
    def get_bus_type(busType):
        try:
            if busType == "SchoolBus":
                return SchoolBus()
            elif busType == "CollegeBus":
                return CollegeBus()
            elif busType == "UniversityBus":
                return UniversityBus()

            raise AssertionError("Bus not found")

        except AssertionError as _e:
            print(_e)


if __name__ == "__main__":
    bus_factory = BusFactory.get_bus_type("SchoolBus")
    print(bus_factory.get_bus_dimensions())
    bus_factory = BusFactory.get_bus_type("CollegeBus")
    print(bus_factory.get_bus_dimensions())
    bus_factory = BusFactory.get_bus_type("UniversityBus")
    print(bus_factory.get_bus_dimensions())
