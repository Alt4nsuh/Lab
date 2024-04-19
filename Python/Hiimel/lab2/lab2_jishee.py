import random
class Agent:
    pass

class RandomAgent(Agent):
    def __init__(self, actions):
        Agent.__init__(self)
        self.actions = actions

    def program(self, percept):
        return random.choice(self.actions)

def randomvacuumagent():
    print("Вакуум орчноос нэг үйлдлийг санамсаргүй байдлаар сонгоно")
    percept = "Dirty"
    actions = ['Right', 'Left', 'Suck', 'NoOp']
    agent = RandomAgent(actions)
    action = agent.program(percept)
    print("Selected action:", action)

randomvacuumagent()