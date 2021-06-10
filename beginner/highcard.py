from cardreader import *


def high_cards(p1_cards, p2_cards):
    p1_ranks = cards2rank(p1_cards)
    p1_ranks.sort(reverse=True)
    p2_ranks = cards2rank(p2_cards)
    p2_ranks.sort(reverse=True)
    print(p1_ranks, p2_ranks)
    for index in range(2):
        p1_ranks.pop(min(p1_ranks))
        p2_ranks.pop(min(p2_ranks))
        print(p1_ranks)
        print(p2_ranks)
    for index in range(len(p1_ranks)):
        if p1_ranks[index] == p2_ranks[index]:
            continue
        elif p1_ranks[index] > p2_ranks[index]:
            return 'p1'
        elif p2_ranks[index] > p1_ranks[index]:
            return 'p2'
    else:
        return 'draw'


