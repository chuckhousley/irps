__author__ = 'Chuck'
import glb as g
from player import player_choice
from opponent import opponent_choice
from operators import winner, score


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
        am.pop()
        am.insert(0, (player, opponent))

    # plays remaining l-2k games while recording fitness
    test = g.l-2*g.k
    for i in range(g.l - 2*g.k):
        player = player_choice(am, st)
        opponent = opponent_choice(am, os)
        player_score += score(player, opponent)
        am.pop()
        am.insert(0, (player, opponent))

    return player_score
