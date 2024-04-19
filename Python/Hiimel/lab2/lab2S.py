
import random
class Room:
    def __init__(self, size=8):
        self.size = size
        self.grid = [['Dirty' if random.random() < 0.5 else 'Clean' for _ in range(size)] for _ in range(size)]
        self.room_names = {f'Room_{i}_{j}' for i in range(size) for j in range(size)}

 
    def get_state(self, x, y):
        return self.grid[x][y]

    def clean_tile(self, x, y):
        self.grid[x][y] = 'Clean'

class vacuum:
    def __init__(self, name):
        self.name = name
        self.location = (0, 0)
        self.performance = 0
        self.cleaned_rooms = set()

    def state(self, room):
        x, y = self.location
        return room.get_state(x, y)

    def clean(self):
        self.performance += 1

    def move(self, direction):
        x, y = self.location
        if direction == 'Up' and x > 0:
            self.location = (x - 1, y)
        elif direction == 'Down' and x < 7:
            self.location = (x + 1, y)
        elif direction == 'Left' and y > 0:
            self.location = (x, y - 1)
        elif direction == 'Right' and y < 7:
            self.location = (x, y + 1)

    def decide_action(self, state):
        if state == 'Dirty':
            return 'Clean'
        elif self.location[0] % 2 == 0:
            if self.location[1] < 7:
                return 'Right'
            else:
                return 'Down'
        else:
            if self.location[1] > 0:
                return 'Left'
            else:
                return 'Down'

    def pour_garbage(self, room):
        print(f"{self.name} hogoo asgaj bna.")
        self.performance = 0

    def run(self, room):
        battery = 100
        for _ in range(100):
            current_state = self.state(room)
            action = self.decide_action(current_state)

            if action == 'Clean':
                self.clean()
                x, y = self.location
                room.clean_tile(x, y)
                room_name = f'Room_{x}_{y}'
                self.cleaned_rooms.add((room_name, self.performance))
            elif action in ['Up', 'Down', 'Left', 'Right']:
                self.move(action)

            x, y = self.location
            battery -= 1

            print(f"{self.name} location: {self.location}")
            print(f"Cleaned tiles: {self.performance}")
            print(f"Battery remaining: {battery}")

            if self.performance >= 20:
                self.pour_garbage(room)

            if battery == 0:
                print(f"{self.name} ran out of battery")
                break

        print("Cleaned rooms:")
        for room_info in self.cleaned_rooms:
            print(f"{room_info[0]}")

room1 = Room()
agent = vacuum(name='ToosSorogch')
agent.run(room1)
