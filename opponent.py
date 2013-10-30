__author__ = 'Chuck'
import glb as g
from operators import winner


def opponent_choice(am, os):
    return _last_winner(am) if g.o_strat == 'last' else _csv(am, os)


def _last_winner(am):
    return winner(am[0][0], am[0][1])


def _csv(am, os):
    if not os:
        print 'No csv file to read from!'
        exit()
    k = os['k']
    prev_moves = ''
    for mem in am:
        prev_moves += mem[0] + mem[1]
    return os[prev_moves[:k]]