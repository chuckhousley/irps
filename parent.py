__author__ = 'Chuck'
import glb as g
from gpTree import *
from generate import *
from game import play_2b, play_2c
from sys import maxint
from log import write_log
from math import ceil


def parents(survivors):
    if g.parent == 'fps':
        return _fps(survivors)
    elif g.parent == 'os':
        return _os(survivors)


def _fps(survivors):  # fitness proportional search
    selection = []
    for i in range(len(survivors)):
        amount_to_add = survivors[i].fitness if survivors[i].fitness > 0 else 1
        for j in range(amount_to_add):
            selection.append(i)

    assert len(selection) > 1
    parent1 = g.rand.choice(selection)
    parent2 = g.rand.choice(selection)
    while parent1 == parent2:
        parent2 = g.rand.choice(selection)

    return survivors[parent1], survivors[parent2]


def _os(survivors):  # over-selection
    plebeian = list(survivors)
    patrician = []

    higher = int(round(len(plebeian)*0.2))  # size of top 20% of survivors
    higher = higher if higher > 0 else 1  # makes sure at least 1 element is in patrician list

    while len(patrician) <= higher:
        high_score = -maxint
        best_element = -1
        for j in range(len(plebeian)):
            if plebeian[j].fitness > high_score:
                high_score = plebeian[j].fitness
                best_element = j
        assert best_element > -1
        patrician.append(plebeian.pop(best_element))

    return g.rand.choice(patrician), g.rand.choice(plebeian)


def create_parents_2b():
    os = generate_opponent_csv() if g.o_strat != 'last' else None
    survivors = []
    for initial_parents in range(g.mu):
        new_parent = gpTree(generate_strategy_tree())
        am = generate_agent_mem()
        new_parent.fitness = play_2b(am, new_parent.tree, os)
        survivors.append(new_parent)
    return survivors


def create_parents_2c(log):
    survivors = []
    evals = 0
    for initial_parents in range(g.mu):
        survivors.append(gpTree(generate_strategy_tree()))

    for ip in survivors:
        temp = list(survivors)  # creates a copy of the survivor list
        temp.remove(ip)         # and removes the current item so it doesn't battle itself

        fitness = 0
        num_opponents = int(ceil(len(temp)*g.percent))
        for op in g.rand.sample(temp, num_opponents):
            am = generate_agent_mem()
            fitness += play_2c(am, ip.tree, op.tree)
            evals += 1
        ip.fitness = float(fitness)/num_opponents  # assigns fitness to be average fitness over all opponents

    write_log(log, survivors, evals)
    return survivors, evals
