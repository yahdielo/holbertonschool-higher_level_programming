#!/usr/bin/python3

def multiple_returns(sentence):

    count = 0

    if sentence is None:
        sentence[0] = None 
        _tuple = (count, sentence[0])
        return _tuple
    else:
        for i in  sentence:
            count += 1

    _tuple = (count, sentence[0])

    return _tuple
