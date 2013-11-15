__author__ = 'Chuck'
from sys import argv
from time import time
import glb as g
from log import *
from generate import *
from game import play_2a


def main():
    tic = time()
    #again with the one line of arguments input
    cfg = argv[2] if (len(argv) == 3 and argv[1] == '-c') else 'default.cfg'
    g.init(cfg)

    best_st = assignment_2a()
    write_soln(best_st)
    toc = time()
    print 'Execution time: %.2f seconds' % (toc-tic)

if __name__ == '__main__':
    main()