__author__ = 'Chuck'
from sys import argv
import glb as g
from log import prepare_log
from operators import winner


def main():
    #again with the one line of arguments input
    cfg = argv[2] if (len(argv) == 3 and argv[1] == '-c') else 'default.cfg'
    g.init(cfg)

    prepare_log()
    print winner('p', 'r')
    print winner('s', 'r')
    print winner('p', 'p')



if __name__ == '__main__':
    main()