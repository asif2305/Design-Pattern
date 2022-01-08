from abc import ABCMeta, abstractstaticmethod


class ITable(metaclass=ABCMeta):

    @staticmethod
    def get_dimensions():
        """The Table Interface"""


class BigTable(ITable):

    def __init__(self):
        self.height = 90
        self.width = 90
        self.depth = 90

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class MediumTable(ITable):

    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class SmallTable(ITable):

    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class TableFactory():

    @staticmethod
    def get_table_type(table_type):

        try:
            if table_type == "BigTable":
                return BigTable()
            elif table_type =="MediumTable":
                return MediumTable()

            elif table_type == "SmallTable" :
                return SmallTable()
            raise AssertionError("Table not available ")
        except AssertionError as _e:
            print(_e)


"""
if __name__ == "__main__":
    table_factory = TableFactory.get_chair_type("BigTable")
    print(table_factory.get_dimensions())
    chair_factory = TableFactory.get_chair_type("MediumTable")
    print(table_factory.get_dimensions())
    chair_factory = TableFactory.get_chair_type("SmallTable")
    print(table_factory.get_dimensions())
"""