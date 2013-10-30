__author__ = 'Chuck'
from sys import argv
import glb as g
from log import prepare_log
from generate import *
from player import *

# todo log and solution files
# todo opponent strategies
# todo operations on agent memory list
# todo add gt to specific log file


def main():
    #again with the one line of arguments input
    cfg = argv[2] if (len(argv) == 3 and argv[1] == '-c') else 'default.cfg'
    g.init(cfg)
    am = generate_agent_mem()
    st = generate_strategy_tree()
    generate_opponent_csv()
    #prepare_log(log)



if __name__ == '__main__':
    main()