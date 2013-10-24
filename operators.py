__author__ = 'Chuck'


# returns the winner of two inputs, the winner is based on the payoff matrix.
# if both inputs are equal, then the output will be the input
def winner(a, b):
    if a == b:
        return a
    if (a, b).count('r') and (a, b).count('p'):
        return 'p'
    if (a, b).count('p') and (a, b).count('s'):
        return 's'
    if (a, b).count('r') and (a, b).count('s'):
        return 'r'


# returns the loser of two inputs, the loser is based on the payoff matrix
# if both inputs are equal, then the output will be the input
def loser(a, b):
    if a == b:
        return a
    if (a, b).count('r') and (a, b).count('p'):
        return 'r'
    if (a, b).count('p') and (a, b).count('s'):
        return 'p'
    if (a, b).count('r') and (a, b).count('s'):
        return 's'


# returns the input choice that is neither of the two inputs
# inputs of rock and paper return scissors, paper and scissors returns rock, and rock and scissors returns paper
# if inputs are equal, the next letter in the 'rps' sequence is returned (r -> p -> s -> r -> p -> s...)
def other(a, b):
    if a == b == 'r':
        return 'p'
    if a == b == 'p':
        return 's'
    if a == b == 's':
        return 'r'
    if (a, b).count('r') and (a, b).count('p'):
        return 's'
    if (a, b).count('p') and (a, b).count('s'):
        return 'r'
    if (a, b).count('r') and (a, b).count('s'):
        return 'p'