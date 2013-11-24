__author__ = 'Chuck'
from sys import argv
from time import time
import glb as g
import rate as r
from assignment import *


def main():
    tic = time()
    #again with the one line of arguments input
    cfg = argv[2] if (len(argv) == 3 and argv[1] == '-c') else 'default.cfg'
    g.init(cfg)
    r.init()

    #assignment_2a()
    #assignment_2b()
    assignment_2c()

    print "Win: {0}\tLose: {1}\tDraw: {2}\n".format(r.w, r.l, r.d)

    toc = time()
    print 'Execution time: %.2f seconds\n' % (toc-tic)

if __name__ == '__main__':
    main()