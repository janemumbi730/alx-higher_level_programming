#!/usr/bin/python3
def multiple_returns(sentence):
    i = len(sentence)

    if (i == 0):
        j = (i, None)
    else:
        j = (i, sentence[0])

    return (j)
