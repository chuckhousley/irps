__author__ = 'Chuck'
import glb as g
from gpTree import *
from log import *
from generate import *
from game import *
from parent import create_parents
from child import create_children
from sys import maxint


def assignment_2a():
    os = generate_opponent_csv() if g.o_strat != 'last' else None
    log = open(g.log, 'w')
    prepare_log(log)

    best_score = -1
    best_st = None

    for i in range(g.evals):
        am = generate_agent_mem()
        st = generate_strategy_tree()
        new_score = play_2a(am, st, os)
        if new_score > best_score:
            log.write('{0}\t{1}\n'.format(i, new_score))
            best_score = new_score
            best_st = st

    log.close()
    write_soln(best_st)


def assignment_2b():
    # initializing functions

    log = open(g.log, 'w')
    prepare_log(log)

    best_fitness = -maxint
    best_tree = None

    for i in range(g.runs):
        log.write("Run {0}\n".format(i+1))
        print "Starting Run {0}\n".format(i+1)
        # create first mu parents
        survivors = create_parents()

        previous_max = -maxint
        termination_count = 0
        evals = g.mu
        write_log(log, survivors, evals)

        while evals < g.evals:
            children = create_children(survivors)
            evals += g.lam

            for c in children:  # mu+lambda
                survivors.append(c)

            for s in survivors:
                if len(s.tree) > (2**(g.d+1) - 1):
                    s.fitness *= g.p

            if g.survival == 't':
                while len(survivors) > g.mu:
                    lowest = maxint
                    truncated_tree = -1
                    for s in survivors:
                        if s.fitness < lowest:
                            lowest = s.fitness
                            truncated_tree = s
                    survivors.remove(truncated_tree)

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

            else:
                print 'invalid termination choice, please update .cfg file'

            current_max = -maxint
            for s in survivors:
                if s.fitness > current_max:
                    current_max = s.fitness
            if current_max == previous_max:
                termination_count += 1
            else:
                previous_max = current_max
                termination_count = 0
            if termination_count == g.n and g.termination == 'nc':
                break

            for s in survivors:
                if s.fitness > best_fitness:
                    best_fitness = s.fitness
                    best_tree = s.tree

            write_log(log, survivors, evals)

    write_soln(best_tree)
