__author__ = 'Chuck'
from random import Random, randint
from sys import maxint


def error():
    print "Invalid input. Please check command line arguments and config file for errors"
    exit()


def init(cfg):
    global o_strat
    global runs
    global l
    global k
    global d
    global seed
    global rand
    global log
    global log_name
    global soln
    global payoff

    o_strat = None
    runs = None
    rand = None
    l = None
    k = None
    d = None
    seed = None
    log = None
    log_name = None
    soln = None
    payoff = dict()

    try:
        f = open(cfg, 'r')
    except IOError:
        print "failed to open", cfg
        error()

    for line in f:
        line = line.split('=')
        if len(line) != 2 or line[1] == '':
            continue
        else:
            line[0] = line[0].strip()
            line[1] = line[1].strip()

        if line[0] == 'os':
            o_strat = line[1]
        elif line[0] == 'runs':
            try:
                runs = int(line[1])
            except ValueError:
                print 'Runs'
                error()
        elif line[0] == 'l':
            try:
                l = int(line[1])
            except ValueError:
                print 'l'
                error()
        elif line[0] == 'k':
            try:
                k = int(line[1])
            except ValueError:
                print 'k'
                error()
        elif line[0] == 'd':
            try:
                d = int(line[1])
            except ValueError:
                print 'd'
                error()
        elif line[0] == 'seed':
            try:
                seed = int(line[1])
            except ValueError:
                print 'seed'
                error()
        elif line[0] == 'log':
            log_name = line[1]
        elif line[0] == 'soln':
            soln = line[1]

        # I'm just going to assume the matrix is correctly formatted
        elif line[0] == 'R':
            rock = line[1].split('|')
            payoff['r_r'] = int(rock[0])
            payoff['p_r'] = int(rock[1])
            payoff['s_r'] = int(rock[2])
        elif line[0] == 'P':
            paper = line[1].split('|')
            payoff['r_p'] = int(paper[0])
            payoff['p_p'] = int(paper[1])
            payoff['s_p'] = int(paper[2])
        elif line[0] == 'S':
            scissors = line[1].split('|')
            payoff['r_s'] = int(scissors[0])
            payoff['p_s'] = int(scissors[1])
            payoff['s_s'] = int(scissors[2])
    f.close()

    if not seed:
        seed = randint(0, maxint)
    rand = Random(seed)

    log = open(log_name, 'w')