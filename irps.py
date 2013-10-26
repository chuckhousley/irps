__author__ = 'Chuck'
from sys import argv
import glb as g
from log import prepare_log
from generate import *
from operators import winner

# todo make function to return value from list from string input
# todo log and solution files
# todo read in csv file
# todo opponent strategies
# todo operations on agent memory list
# todo add gt to specific log file


def main():
    #again with the one line of arguments input
    cfg = argv[2] if (len(argv) == 3 and argv[1] == '-c') else 'default.cfg'
    g.init(cfg)
    am = generate_agent_mem()
    st = generate_strategy_tree()
    # i make a change
    #prepare_log(log)


if __name__ == '__main__':
    main()