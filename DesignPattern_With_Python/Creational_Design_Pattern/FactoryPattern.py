# Resource
#    

from abc import ABCMeta, abstractstaticmethod

"""
Factory method is a creational design pattern that provides an interface for creating 
object in a superclass, but allows subclasses to alter the type of object 
that will be created
It is used when we don't know how many or what type of objects will be needed until during runtime
"""

"""
Pros:
 1. Avoid tight coupling between the creator and the concrete products.
 2. Single Responsibility Principle: Move the product creation code into one place in the program, 
 making the code easier to support.
 3. Open/Closed Principle : Introduce new types of products into the program without breaking existing client code.

Cons:
1. The code may become more complicated to introduce a lot of new subclasses to implement the pattern. 
The best case scenario is to introducing the pattern into an existing hierarchy of creator classes.
"""

# declare a interface
class IBus(metaclass=ABCMeta):

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


