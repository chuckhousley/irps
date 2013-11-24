__author__ = 'Chuck'
import glb as g
import rate as r
from player import player_choice
from opponent import opponent_choice
from operators import winner, score
from generate import generate_agent_mem


def update_rate(p, o):
    if p == o:
        r.d += 1
    elif (p == 'p' and o == 'r') or (p == 'r' and o == 's') or (p == 's' and o == 'p'):
        r.w += 1
    else:
        r.l += 1


def play_2a(am, st, os):
    player_score = 0
    for i in range(g.l):
        player = player_choice(am, st)
        opponent = opponent_choice(am, os)
        if player != opponent and player == winner(player, opponent):
            player_score += 1
        am.pop()
        am.insert(0, (player, opponent))
    return float((float(player_score)/float(g.l)*100))


def play_2b(am, st, os):
    player_score = 0
    # plays 2k games as warm-up for agent memory (I guess)
    for i in range(2*g.k):
        player = player_choice(am, st)
        opponent = opponent_choice(am, os)
        update_rate(player, opponent)
        am.pop()
        am.insert(0, (player, opponent))

    # plays remaining l-2k games while recording fitness
    for i in range(g.l - 2*g.k):
        player = player_choice(am, st)
        opponent = opponent_choice(am, os)
        update_rate(player, opponent)
        player_score += score(player, opponent)
        am.pop()
        am.insert(0, (player, opponent))

    return player_score


def play_2c(am, st1, st2):  # plays coevolutionary games
    fitness = 0
    # plays 2k games as warm-up for agent memory (I guess)
    for i in range(2*g.k):
        player = player_choice(am, st1)
        opponent = player_choice(am, st2)
        update_rate(player, opponent)
        am.pop()
        am.insert(0, (player, opponent))

    # plays remaining l-2k games while recording fitness
    for i in range(g.l - 2*g.k):
        player = player_choice(am, st1)
        opponent = player_choice(am, st2)
        update_rate(player, opponent)
        fitness += score(player, opponent)
        am.pop()
        am.insert(0, (player, opponent))

    return fitness

