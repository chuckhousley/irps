__author__ = 'Chuck'
import glb as g
from operators import winner


def opponent_choice(am, os=None):
    return _last_winner(am) if g.o_strat == 'last' else _csv(ip, os)


def _last_winner(am):
    return winner(am[0][0], am[0][1])


def _csv(ip, os):
    if not os:
        print 'No csv file to read from!'
        exit()
