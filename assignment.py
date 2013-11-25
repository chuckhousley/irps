__author__ = 'Chuck'
import glb as g
from gpTree import *
from log import *
from generate import *
from game import *
from survival import *
from parent import create_parents_2b, create_parents_2c
from child import create_children_2b, create_children_2c
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
        survivors = create_parents_2b()

        previous_avg = -maxint
        termination_count = 0
        evals = g.mu
        write_log(log, survivors, evals)

        while evals < g.evals:
            children = create_children_2b(survivors)
            evals += g.lam

            survivors = strategy(survivors, children)

            parsimony(survivors)

            survivors = remove_the_weak(survivors)

            if g.termination == 'nc':
                current_avg = average_fit(survivors)
                if current_avg == previous_avg:
                    termination_count += 1
                else:
                    previous_avg = current_avg
                    termination_count = 0
                if termination_count == g.n:
                    break

            for s in survivors:
                if s.fitness > best_fitness:
                    best_fitness = s.fitness
                    best_tree = s.tree

            write_log(log, survivors, evals)

    write_soln(best_tree)


def assignment_2c():
    # initializing functions
    log = open(g.log, 'w')
    prepare_log(log)

    best_fitness = -maxint
    best_tree = None

    for i in range(g.runs):
        log.write("\nRun {0}\n".format(i+1))
        print "Starting Run {0}\n".format(i+1)
        survivors, evals = create_parents_2c(log)

        previous_avg = -maxint
        termination_count = 0

        hall_of_fame = []

        while evals < g.evals:
            children, children_evals = create_children_2c(survivors)
            evals += children_evals

            survivors = strategy(survivors, children)

            parsimony(survivors)

            survivors = remove_the_weak(survivors)
            assert len(survivors) == g.mu

            update_hof(survivors, hall_of_fame)

            current_avg = average_fit(survivors)
            if current_avg < previous_avg:  # cycling detected
                use_hof(survivors, hall_of_fame)
            elif current_avg == previous_avg:
                termination_count += 1
            else:
                previous_avg = current_avg
                termination_count = 0
            if termination_count == g.n and g.termination == 'nc':
                break

            for s in survivors:
                if s.fitness > best_fitness:
                    best_fitness = s.fitness
                    best_tree = s.tree

            write_log(log, survivors, evals)

    # Play the best tree against the opponent strategies
    log.write('\nAbsolute Fitness\n')
    am = generate_agent_mem()
    os = generate_opponent_csv() if g.o_strat != 'last' else None
    abs_fitness = play_2b(am, best_tree, os)

    log.write(str(abs_fitness))
    log.close()

    write_soln(best_tree)
