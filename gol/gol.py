class myapp:
    
    world = None

    def __init__(self):
        pass
    
    def create_world(self):
        self.world = []
    
    def world_exists(self):
        if self.world == None:
            return False
        elif self.world == []:
            return True


if __name__ == "__main__":
    myapp()