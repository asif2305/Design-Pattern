
from abc import ABCMeta ,abstractstaticmethod

"""
Builder Design Pattern:
The builder design pattern is a creational pattern whose intent is to separate the construction
of a complex object from its representaions so that you can use the same construction process
to create different representations

The pattern tries to solve : 
- How can a class create different representations of a complex object?
- How can a class that includes creating a complex object be simplified? 
"""
class IHouseBuilder(metaclass= ABCMeta):
    """ The builder interface """
    @staticmethod
    def set_wall_material(self,value):
        """ Set the wall_material """

    @staticmethod
    def set_building_type(self,value):
        """ Set the building_type """

    @staticmethod
    def set_number_doors(self,value):
        """Set the number of doors"""

    @staticmethod
    def set_number_windows(self):
        """Set the number of windows"""

    @staticmethod
    def get_result(self):
        """Return the house"""
