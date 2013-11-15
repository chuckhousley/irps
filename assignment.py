__author__ = 'Chuck'


def assignment_2a():
    os = generate_opponent_csv() if g.o_strat != 'last' else None
    log = open(g.log, 'w')
    prepare_log(log)

    score = -1
    best_st = None

    for i in range(g.runs):
        am = generate_agent_mem()
        st = generate_strategy_tree()
        new_score = play_2a(am, st, os)
        if new_score > score:
            log.write('{0}\t{1}\n'.format(i, new_score))
            score = new_score
            best_st = st

    log.close()
    return best_st


def assignment_2b():
    pass