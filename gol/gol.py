from cell import *

class Gol:
    
    world = None

    def __init__(self):
        pass
    
    def create_world(self, rows, columns):
        self.world = [[0 for x in range(columns)] for y in range(rows)]
    
    def world_exists(self):
        if not self.world:
            return False
        else:
            return True

    def populate_world(self):
        for i in range(len(self.world)):
            for j in range(len(self.world[i])):
                self.world[i][j] = Cell()

    def world_is_populated(self):
        return self.world[0][0].cexists()


if __name__ == "__main__":
    myapp()