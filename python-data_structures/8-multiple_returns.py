#!/usr/bin/python3


def multiple_returns(sentence):
    count = 0

    if sentence is None or len(sentence) == 0:
        _tuple = (count, None)
        return _tuple
    else:
        count = len(sentence)

    _tuple = (count, sentence[0])

    return _tuple
