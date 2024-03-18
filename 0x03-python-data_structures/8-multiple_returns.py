#!/usr/bin/python3
def multiple_returns(sentence):
    answer = []
    answer.append(len(sentence))
    if len(sentence) == 0:
        answer.append(None)
    else:
        answer.append(sentence[0])

    return answer
