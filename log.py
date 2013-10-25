__author__ = 'Chuck'
import glb as g


def prepare_log(log):
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