__author__ = 'Chuck'
import glb as g
from player import player_choice
from opponent import opponent_choice
from operators import winner


def play(am, st, os):
    player_score = 0
    t_tie = 0
    t_lose = 0
    for i in range(g.l):
        player = player_choice(am, st)
        opponent = opponent_choice(am, os)
        if player == opponent:
            t_tie += 1
        elif player != opponent and player == winner(player, opponent):
            player_score += 1
        else:
            t_lose += 1
        am.pop()
        am.insert(0, (player, opponent))
    return float((float(player_score)/float(g.l)*100))
