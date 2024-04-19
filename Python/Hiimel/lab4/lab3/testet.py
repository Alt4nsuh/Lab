import time

class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self, state):
        raise NotImplementedError


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        return [self.child_node(problem, action) for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


import sys
from collections import deque


class NQueensProblem(Problem):
    def __init__(self, N):
        super().__init__(tuple([-1] * N))
        self.N = N

    def actions(self, state):
        if state[-1] != -1:
            return []
        else:
            col = state.index(-1)
            return [row for row in range(self.N) if not self.conflicted(state, row, col)]

    def result(self, state, row):
        col = state.index(-1)
        new = list(state[:])
        new[col] = row
        return tuple(new)

    def conflicted(self, state, row, col):
        return any(self.conflict(row, col, state[c], c) for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        return (
            row1 == row2 or
            col1 == col2 or
            row1 - col1 == row2 - col2 or
            row1 + col1 == row2 + col2
        )

    def goal_test(self, state):
        if state[-1] == -1:
            return False
        return not any(self.conflicted(state, state[col], col) for col in range(len(state)))

    def h(self, node):
        num_conflicts = 0
        for (r1, c1) in enumerate(node.state):
            for (r2, c2) in enumerate(node.state):
                if (r1, c1) != (r2, c2):
                    num_conflicts += self.conflict(r1, c1, r2, c2)
        return num_conflicts


def breadth_first_tree_search(problem):
    frontier = deque([Node(problem.initial)])  # FIFO queue
    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None


def depth_first_tree_search(problem):
    frontier = [Node(problem.initial)]  # Stack
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None
N=14
start_time = time.time()
gnode = breadth_first_tree_search(NQueensProblem(N))
end_time = time.time()
print("time breadth {:.6f}".format(end_time - start_time))
print(gnode)
start_time = time.time()
gnode = depth_first_tree_search(NQueensProblem(N))
end_time = time.time()
print("time depth {:.6f}".format(end_time - start_time))
print(gnode)