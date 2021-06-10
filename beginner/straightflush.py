from beginner.straight import *
from beginner.flush import *
from beginner.cardreader import *


def check_straight_flush(cards):
    flush, suit, f_high, card_dict = check_flush(cards)
    flush_list = []
    if flush:
        for card in card_dict:
            if card['suit'] == suit:
                flush_list.append(dict2card(card))
        print(flush_list)
        straight, s_high = check_straight(flush_list)
        if straight:
            return True
        else:
            return False
    else:
        return False


# sample = ['Kh', '8h', 'Jh', 'Qh', '6h', '2h', '10h']
# s, h, f = straight_flush(sample)
# print(s)
# print(f)