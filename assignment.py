__author__ = 'Chuck'
import glb as g
from gpTree import *
from log import *
from generate import *
from game import *
from parent import create_parents
from child import create_children


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

    # log = open(g.log, w)
    # prepare_log(log)

    # create first mu parents
    survivors = create_parents()
    children = []






