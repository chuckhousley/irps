__author__ = 'Chuck'
import glb as g
from generate import *
from gpTree import *
from game import play_2b, play_2c
from parent import parents
from math import ceil


def subtree(tree):
    operators = 'WINNER', 'LOSER', 'OTHER'
    root = g.rand.choice(range(len(tree)))
    if tree[root] not in operators:
        return root, root
    else:
        end = root + 1
        stack = ['o']
        while stack[0] != 't':
            if tree[end] in operators:
                stack.append('o')
            else:
                stack.append('t')
            end += 1
            if len(stack) >= 3:
                finish_eval = False
                while not finish_eval:
                    if len(stack) < 3:
                        finish_eval = True
                    elif stack[-3] == 'o' and stack[-2] == stack[-1] == 't':
                        stack.pop()
                        stack.pop()
                        stack[-1] = 't'
                    else:
                        finish_eval = True
    return root, end-1


def create_children_2b(survivors):
    os = generate_opponent_csv() if g.o_strat != 'last' else None
    children = []
    for nc in range(g.lam):
        # parent selection, 2 parents (arbitrary choice)
        parent1, parent2 = parents(survivors)

        # equal chance of parents being flipped for fairness since parent1 is always the
        # mutated parent and parent2 is the mutator
        if g.rand.choice([0, 1]):
            parent1, parent2 = parent2, parent1

        # small chance for mutation
        if g.rand.random() < g.mutation:  # replaces parent2 with a fresh gp tree
            parent2 = gpTree(generate_strategy_tree())  # and a subtree will be generated from this new tree

        new_child = gpTree(list(parent1.tree))
        root1, end1 = subtree(new_child.tree)  # the subtree to be erased
        root2, end2 = subtree(parent2.tree)    # the subtree to be inserted

        # erase old subtree
        for i in range(end1+1 - root1):
            new_child.tree.pop(root1)
        # insert new subtree
        for i in reversed(range(root2, end2+1)):
            new_child.tree.insert(root1, parent2.tree[i])

        # plays games to generate new child's fitness
        am = generate_agent_mem()
        #new_child.fitness = play_2c(am, new_child.tree, generate_strategy_tree())
        new_child.fitness = play_2b(am, new_child.tree, os)
        children.append(new_child)
    return children


def create_children_2c(survivors):
    children = []
    evals = 0
    for nc in range(g.lam):
        # parent selection, 2 parents (arbitrary choice)
        parent1, parent2 = parents(survivors)

        # equal chance of parents being flipped for fairness since parent1 is always the
        # mutated parent and parent2 is the mutator
        if g.rand.choice([0, 1]):
            parent1, parent2 = parent2, parent1

        # small chance for mutation
        if g.rand.random() < 0.01:  # replaces parent2 with a fresh gp tree
            parent2 = gpTree(generate_strategy_tree())  # and a subtree will be generated from this new tree

        new_child = gpTree(list(parent1.tree))
        root1, end1 = subtree(new_child.tree)  # the subtree to be erased
        root2, end2 = subtree(parent2.tree)    # the subtree to be inserted

        # erase old subtree
        for i in range(end1+1 - root1):
            new_child.tree.pop(root1)
        # insert new subtree
        for i in reversed(range(root2, end2+1)):
            new_child.tree.insert(root1, parent2.tree[i])

        children.append(new_child)

    # new children's fitness
    for child in children:
        population = list(survivors + children)
        population.remove(child)

        fitness = 0
        num_opponents = int(ceil(len(population)*g.percent))
        for op in g.rand.sample(population, num_opponents):
            am = generate_agent_mem()
            fitness += play_2c(am, child.tree, op.tree)
            #fitness += play_2c(am, child.tree, generate_strategy_tree())
            evals += 1
        child.fitness = float(fitness)/num_opponents  # assigns fitness to be average fitness over all opponents

    return children, evals



