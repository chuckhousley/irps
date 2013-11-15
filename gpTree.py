__author__ = 'Chuck'
from generate import generate_strategy_tree


class GPTree:
    def __init__(self):
        self.tree = generate_strategy_tree()
        self.fitness = 0
