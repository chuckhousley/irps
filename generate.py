__author__ = 'Chuck'
import glb as g


def generate_agent_mem():
    letters = 'R', 'P', 'S'
    am = []
    for i in range(g.k):
        am.append((g.rand.choice(letters), g.rand.choice(letters)))
    return am


def generate_strategy_tree():
    letters = 'P', 'O'
    numbers = range(1, g.k+1)
    operators = 'WINNER', 'LOSER', 'OTHER'