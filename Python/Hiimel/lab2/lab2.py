import random

class Object:
    def __init__(self):
        self.location = None

    def __repr__(self):
        return '<%s>' % getattr(self, 'name', self.__class__.__name__)

    def is_alive(self):
        return hasattr(self, 'alive') and self.alive

    def display(self, canvas, x, y, width, height):
        pass

class ToosSorogch:
    def __init__(self):
        self.location = (0, 0)
        self.performance = 0
        self.size = 8  
        
    def state(self, room):
        y = self.location[1]
        return room.get_state(y)

    def clean(self):
        self.performance += 1

    def move(self, direction):
        x, y = self.location

        if direction == 'Up' and x > 0:
            self.location = (x - 1, y)
        elif direction == 'Down' and x < self.size - 1:
            self.location = (x + 1, y)
        elif direction == 'Left' and y > 0:
            self.location = (x, y - 1)
        elif direction == 'Right' and y < self.size - 1:
            self.location = (x, y + 1)

    def decide_action(self, state):
        if state == 'Dirty':
            return 'Clean'
        elif self.location[0] % 2 == 0:
            if self.location[1] < self.size - 1:
                return 'Right'
            else:
                return 'Down'
        else:
            if self.location[1] > 0:
                return 'Left'
            else:
                return 'Down'

    def run(self, room):
        battery = 100
        for battery in range(100):
            current_state = self.state(room)
            action = self.decide_action(current_state)
            if action == 'Clean':
                self.clean()
                y = self.location[1]
                room.clean_tile(y)
            elif action in ['Up', 'Down', 'Left', 'Right']:
                self.move(action)
            y = self.location
            print(f"Toos sorogch bairlal: {self.location}")
            print(f"Battery:", (battery - 100) * -1)
        print("Toos sorogch died")

class ModifiedRoom:
    def __init__(self, size=8):
        self.size = size
        self.grid = ['Dirty' if random.random() < 0.5 else 'Clean' for _ in range(size)]
        print(self.grid)

    def display(self):
        for tile in self.grid:
            print(tile, end=' ')
        print()

    def get_state(self, y):
        return self.grid[y]

    def clean_tile(self, y):
        self.grid[y] = 'Clean'

rooms = ModifiedRoom()
agent = ToosSorogch()
agent.run(rooms)
