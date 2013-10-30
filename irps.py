__author__ = 'Chuck'
from sys import argv
from time import time
import glb as g
from log import *
from generate import *
from game import play


def main():
    tic = time()
    #again with the one line of arguments input
    cfg = argv[2] if (len(argv) == 3 and argv[1] == '-c') else 'default.cfg'
    g.init(cfg)

    os = generate_opponent_csv() if g.o_strat != 'last' else None
    log = open(g.log, 'w')
    prepare_log(log)

    score = -1
    best_st = None

    for i in range(g.evals):
        am = generate_agent_mem()
        st = generate_strategy_tree()
        new_score = play(am, st, os)
        if new_score > score:
            log.write('{0}\t{1}\n'.format(i, new_score))
            score = new_score
            best_st = st

    log.close()
    write_soln(best_st)
    toc = time()
    print 'Execution time: %.2f seconds' % (toc-tic)

if __name__ == '__main__':
    main()