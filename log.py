__author__ = 'Chuck'
import glb as g
from sys import maxint


def prepare_log(log):
    log.write('Results Log:\n')
    log.write('k:\t\t{0}\n'.format(g.k))
    log.write('d:\t\t{0}\n'.format(g.d))
    log.write('seed:\t{0}\n'.format(g.seed))
    log.write('strategy:\t{0}\n'.format(g.o_strat))
    log.write('payoff matrix:\n')
    log.write('op|   Player  |\n')
    log.write('  | R | P | S |\n')
    log.write('--|---|---|---|\n')
    log.write('R | {r_r}   {r_p}   {r_s}\n'.format(**g.payoff))
    log.write('--|---|---|---|\n')
    log.write('P | {p_r}   {p_p}   {p_s}\n'.format(**g.payoff))
    log.write('--|---|---|---|\n')
    log.write('S | {s_r}   {s_p}   {s_s}\n'.format(**g.payoff))
    log.write('--------------\n\n')


def write_log(log, survivors, evals):
    average = 0
    best = -maxint
    for s in survivors:
        average += s.fitness
        if s.fitness > best:
            best = s.fitness
    average /= len(survivors)

    avg_str = '%.2f' % average
    best_str = '%.2f' % best
    log.write("{0}\t{1}\t{2}\n".format(evals, avg_str, best_str))


def write_soln(best_st):
    soln = open(g.soln, 'w')
    soln.write(','.join(best_st))
    soln.close()