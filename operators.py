__author__ = 'Chuck'


# returns the winner of two inputs, the winner is based on the payoff matrix.
# if both inputs are equal, then the output will be the input
def winner(a, b):
    if a == b:
        return a
    if (a == 'r' and b == 'p') or (a == 'p' and b == 'r'):
        return 'p'
    if (a == 'p' and b == 's') or (a == 's' and b == 'p'):
        return 's'
    if (a == 'r' and b == 's') or (a == 's' and b == 'r'):
        return 'r'


# returns the loser of two inputs, the loser is based on the payoff matrix
# if both inputs are equal, then the output will be the input
def loser(a, b):
    if a == b:
        return a
    if (a == 'r' and b == 'p') or (a == 'p' and b == 'r'):
        return 'r'
    if (a == 'p' and b == 's') or (a == 's' and b == 'p'):
        return 'p'
    if (a == 'r' and b == 's') or (a == 's' and b == 'r'):
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
    if (a == 'r' and b == 'p') or (a == 'p' and b == 'r'):
        return 's'
    if (a == 'p' and b == 's') or (a == 's' and b == 'p'):
        return 'r'
    if (a == 'r' and b == 's') or (a == 's' and b == 'r'):
        return 'p'