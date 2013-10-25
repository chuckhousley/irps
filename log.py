__author__ = 'Chuck'
import glb


def prepare_log():
    glb.log.write('k:\t\t{0}\n'.format(glb.k))
    glb.log.write('d:\t\t{0}\n'.format(glb.d))
    glb.log.write('seed:\t{0}\n'.format(glb.seed))
    glb.log.write('strategy:\t{0}\n'.format(glb.o_strat))
    glb.log.write('payoff matrix:\n')
    glb.log.write('op|   Player  |\n')
    glb.log.write('  | R | P | S |\n')
    glb.log.write('--|---|---|---|\n')
    glb.log.write('R | {r_r}   {r_p}   {r_s}\n'.format(**glb.payoff))
    glb.log.write('--|---|---|---|\n')
    glb.log.write('P | {p_r}   {p_p}   {p_s}\n'.format(**glb.payoff))
    glb.log.write('--|---|---|---|\n')
    glb.log.write('S | {s_r}   {s_p}   {s_s}\n'.format(**glb.payoff))
    glb.log.write('--------------\n\n')