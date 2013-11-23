__author__ = 'Chuck'
import glb as g


def strategy(survivors, children):
    if g.strategy == 'plus':
        for c in children:  # mu+lambda
                survivors.append(c)
    elif g.strategy == 'comma':
        survivors = list(children)
    else:
        print "strategy not recognized, please update .cfg file"
        exit()  # I'm exiting in a library function AND YOU CAN'T STOP ME

    return survivors


