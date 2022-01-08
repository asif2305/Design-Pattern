from abc import ABCMeta, abstractstaticmethod


class IChair(metaclass=ABCMeta):

    @staticmethod
    def get_dimensions():
        """The Chair Interface"""


class BigChair(IChair):

    def __init__(self):
        self.height = 90
        self.width = 90
        self.depth = 90

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class MediumChair(IChair):

    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class SmallChair(IChair):

    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class ChairFactory():

    @staticmethod
    def get_chair_type(chair_type):

        try:
            if chair_type == "BigChair":
                return BigChair()
            elif chair_type =="MediumChair":
                return MediumChair()

            elif chair_type == "SmallChair" :
                return SmallChair()
            raise AssertionError("Chair not available ")
        except AssertionError as _e:
            print(_e)


"""
if __name__ == "__main__":
    chair_factory = ChairFactory.get_chair_type("BigChair")
    print(chair_factory.get_dimensions())
    chair_factory = ChairFactory.get_chair_type("MediumChair")
    print(chair_factory.get_dimensions())
    chair_factory = ChairFactory.get_chair_type("SmallChair")
    print(chair_factory.get_dimensions())
"""