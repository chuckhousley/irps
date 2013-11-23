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
    for s in survivors:
        if len(s.tree) > (2**(g.d+1) - 1):
            s.fitness *= g.p  # reduces fitness if tree size is bigger than size of fullest tree allowed


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
        return

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
        survivors = new_survivors
        return

    else:
        print 'invalid termination choice, please update .cfg file'
        exit()