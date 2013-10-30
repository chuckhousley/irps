__author__ = 'Chuck'
from operators import *


def player_choice(am, st):
    if len(st) == 1:
        return operand_result(am, st[0])  # for 0 depth trees
    stack = []
    operators = 'WINNER', 'LOSER', 'OTHER'
    operands = 'r', 'p', 's'
    for i in range(len(st)):
        if st[i] not in operators:
            stack.append(operand_result(am, st[i]))  # pushes 'r', 'p', or 's' onto the stack
        else:                                        # instead of 'P1', 'O1', 'P2', etc.
            stack.append(st[i])
        if len(stack) < 3:
            continue
        operation_performed = True
        while operation_performed and len(stack) >= 3:
            if stack[-1] in operands and stack[-2] in operands and stack[-3] in operators:
                operand1 = stack.pop()  # if the top of the stack can be evaluated, the operation
                operand2 = stack.pop()  # is performed and the operators and operands are replaced
                operator = stack.pop()  # with the result of the operation
                stack.append(perform_operation(operator, operand1, operand2))
            else:                            # the evaluation is performed again in case the new
                operation_performed = False  # top of the stack can be evaluated
    return stack[0]  # at the end, there is only one item on the stack; the result reached by the strategy tree


def operand_result(am, pm):
    return am[int(pm[1])-1][0 if pm[0] == 'P' else 1]