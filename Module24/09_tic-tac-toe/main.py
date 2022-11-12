class Cell:

    def __init__(self, number, player, busy=False):
        self.number = number
        self.busy = busy
        self.player = player


class Board:

    def __init__(self):
        self.cell = []

    def add_cell(self, cell):
        self.cell.append(cell)


class Player:

    def __init__(self, name):
        self.name = name



