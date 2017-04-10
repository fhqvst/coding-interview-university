from random import randint

def shuffle(data):
    d = list(data)
    return [ d.pop(randint(0, len(d)-1)) for i in range(len(d)) ]
