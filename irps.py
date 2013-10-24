__author__ = 'Chuck'
from sys import argv
import glb as g


def main():
    #again with the one line of arguments input
    cfg = argv[2] if (len(argv) == 3 and argv[1] == '-c') else 'default.cfg'
    g.Glb(cfg)
    print g.k, g.d, g.seed



if __name__ == '__main__':
    main()