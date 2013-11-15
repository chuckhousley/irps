__author__ = 'Chuck'
import glb as g


def generate_agent_mem():
    rps = 'r', 'p', 's'
    am = []
    for i in range(g.k):
        am.append((g.rand.choice(rps), g.rand.choice(rps)))
    return am


def generate_strategy_tree():
    players = 'P', 'O'
    numbers = range(1, g.k+1)
    operators = 'WINNER', 'LOSER', 'OTHER'
    d = g.rand.choice(range(0, g.d+1))

    # lambda functions for randomly generating operators and operands
    # included primarily for readability and less writing
    operator = lambda: g.rand.choice(operators)
    operand = lambda: g.rand.choice(players) + str(g.rand.choice(numbers))

    if d == 0:
        return [operand()]  # if d = 0 then tree is single terminal node
    else:
        st = []
        tree_stack = [(operator(), 0)]  # begins by adding an operator node to the root
                                        # also adds the current depth of the node
        while len(tree_stack) > 0:
            element = tree_stack.pop()
            st.append(element[0])  # as an element is taken off the stack, it is added to the tree
            if element[0] not in operators:  # if the element is a terminal node
                continue                     # the loop continues since nothing is added underneath it

            current_d = element[1] + 1
            if current_d == d:  # adds terminal nodes to the max depth of the tree
                tree_stack.append((operand(), current_d))
                tree_stack.append((operand(), current_d))
            else:
                if g.rand.choice([0, 1]):  # either adds two operators
                    tree_stack.append((operator(), current_d))
                    tree_stack.append((operator(), current_d))
                else:                      # or an operator and a terminal node
                    tree_stack.append((operand(), current_d))   # since no operators depend on order
                    tree_stack.append((operator(), current_d))  # these can be added safely in any order
        return st


def generate_opponent_csv():
    try:
        f = open(g.o_strat, 'r')
    except IOError:
        print "failed to open", g.o_strat
        exit()
    os = {}
    l = list(f)
    f.close()
    k = int(l[0])*2
    os['k'] = k  # stores k in the dict for easy access without making it a global
    for line in l[1:]:
        # this loop:
        #   1. splits each line of the csv file on the commas into a python list
        #   2. joins the list back together into a string with nothing separating the values
        #   3. makes the string all lowercase for standardization purposes
        #   4. hashes the first (k*2)-1 elements so that the kth element (the opponent's choice) can be accessed
        #      by feeding in a string of each of the player's and opponent's previous moves into the dict
        line = ''.join(line[:-1].split(',')).lower()
        os[line[:k]] = line[-1]
    return os

