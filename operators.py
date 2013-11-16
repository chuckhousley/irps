__author__ = 'Chuck'
import glb


def perform_operation(operator, operand1, operand2):
    if operator == 'WINNER':
        return winner(operand1, operand2)
    elif operator == 'LOSER':
        return loser(operand1, operand2)
    elif operator == 'OTHER':
        return other(operand1, operand2)


# returns the score from the payoff matrix for fitness calculation
def score(p, o):
    return glb.payoff['{0}_{1}'.format(p, o)]


# returns the winner of two inputs, the winner is based on the payoff matrix.
# if both inputs are equal, then the output will be the input
def winner(p, o):
    if p == o:
        return p
    return p if glb.payoff['{0}_{1}'.format(p, o)] > 0 else o


# returns the loser of two inputs, the loser is based on the payoff matrix
# if both inputs are equal, then the output will be the input
def loser(p, o):
    if p == o:
        return p
    return p if glb.payoff['{0}_{1}'.format(p, o)] < 0 else o


# returns the input choice that is neither of the two inputs
# inputs of rock and paper return scissors, paper and scissors returns rock, and rock and scissors returns paper
# if inputs are equal, the next letter in the 'rps' sequence is returned (r -> p -> s -> r -> p -> s...)
def other(p, o):
    if p == o == 'r':
        return 'p'
    if p == o == 'p':
        return 's'
    if p == o == 's':
        return 'r'
    if (p, o).count('r') and (p, o).count('p'):
        return 's'
    if (p, o).count('p') and (p, o).count('s'):
        return 'r'
    if (p, o).count('r') and (p, o).count('s'):
        return 'p'