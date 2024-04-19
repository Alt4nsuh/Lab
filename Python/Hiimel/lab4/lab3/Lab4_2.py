import time

class Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move

    def expand(self):
        children = []
        for i, val in enumerate(self.state):
            if val == 0:
                row, col = divmod(i, 3)
                if row > 0:
                    new_state = list(self.state)
                    new_state[i], new_state[i-3] = new_state[i-3], new_state[i]
                    children.append(Node(new_state, self, "Up"))
                if row < 2:
                    new_state = list(self.state)
                    new_state[i], new_state[i+3] = new_state[i+3], new_state[i]
                    children.append(Node(new_state, self, "Down"))
                if col > 0:
                    new_state = list(self.state)
                    new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
                    children.append(Node(new_state, self, "Left"))
                if col < 2:
                    new_state = list(self.state)
                    new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
                    children.append(Node(new_state, self, "Right"))
                break
        return children


def dfs(initial_state):
    initial_node = Node(initial_state)
    frontier = [initial_node]
    explored = set()

    while frontier:
        node = frontier.pop()
        explored.add(tuple(node.state))

        if node.state == goal_state:
            moves = []
            while node.parent:
                moves.append(node.move)
                node = node.parent
            moves.reverse()
            return moves

        for child in node.expand():
            if tuple(child.state) not in explored:
                frontier.append(child)

    return None

initial_state = [1, 2, 3, 4, 5, 0, 6, 7, 8]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

start_time = time.time()
solution = dfs(initial_state)
end_time = time.time()

if solution:
    print("Solution steps:", solution)
    print("Solution found in {:.6f} seconds".format(end_time - start_time))

else:
    print("No solution found.")
