__author__ = 'Chuck'
import glb as g
from sys import maxint


def strategy(survivors, children):
    if g.strategy == 'plus':
        for c in children:  # mu+lambda
                survivors.append(c)
    elif g.strategy == 'comma':
        survivors = list(children)
    else:
        print "strategy not recognized, please update .cfg file"
        exit()  # I'm exiting in a library function AND YOU CAN'T STOP ME
    return survivors


def parsimony(survivors):
    for s in survivors:  # parsimony is applied regardless of size of tree
        s.fitness = float(s.fitness) - len(s.tree)*g.p


def average_fit(survivors):
    average = 0
    for s in survivors:
        average += s.fitness
    average /= len(survivors)
    return average


def remove_the_weak(survivors):
    if g.survival == 't':
        while len(survivors) > g.mu:
            lowest = maxint
            truncated_tree = -1
            for s in survivors:
                if s.fitness < lowest:
                    lowest = s.fitness
                    truncated_tree = s
            survivors.remove(truncated_tree)
        return survivors

    elif g.survival == 'k':
        new_survivors = []
        while len(new_survivors) < g.mu:
            tournament = g.rand.sample(survivors, g.kt)
            highest_score = -maxint
            winning_tree = None
            for t in tournament:
                if t.fitness > highest_score:
                    highest_score = t.fitness
                    winning_tree = t
            new_survivors.append(winning_tree)
            survivors.remove(winning_tree)
        return new_survivors

    else:
        print 'invalid termination choice, please update .cfg file'
        exit()


# EXTRA CREDIT FUNCTIONS #
def update_hof(survivors, hall_of_fame):
    highest_fitness = -maxint
    new_champ = None
    for s in survivors:
        if s.fitness > highest_fitness:
            highest_fitness = s.fitness
            new_champ = s

    if len(hall_of_fame) == g.lam:
        hall_of_fame.pop(0)

    hall_of_fame.append(new_champ)


def use_hof(survivors, hall_of_fame):
    lowest_fitness = maxint
    new_chump = None
    for champ in hall_of_fame:
        for i in range(len(survivors)):
            if survivors[i].fitness < lowest_fitness:
                lowest_fitness = survivors[i].fitness
                new_chump = i
        if new_chump and champ.fitness > survivors[new_chump].fitness:
            survivors.pop(new_chump)
            survivors.append(champ)