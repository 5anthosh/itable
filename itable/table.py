from .printer import cTable, rTable


class Table():

    def __init__(self, row=True, header=False):
        self.row = row
        self.header = header
        self.__table = []
    
    def append(self, layer):
        self.__table.append(list(layer))
    
    def printer(self):
        if self.row :
            rTable(self.__table)
        else:
            cTable(self.__table)
