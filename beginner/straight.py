from cardreader import *


def is_straight(card_dict):
    # TODO this function does not work with a straight longer than 5 cards
    # takes card dict, returns boolean and the high card if it is a straight
    rank_set = {card['rank'] for card in card_dict}
    print(rank_set)
    count = 0
    for rank in (14, *range(2, 15)):
        if rank in rank_set:
            count += 1
            if count == 5:
                return True, rank
        else:
            count = 0
    else:
        return False, False


def straight_high(card_dict):
    # input list of cards, output straight and high card
    straight, high_card = is_straight(card_dict)
    if straight:
        card_name = rank2face(high_card)
        print(f'Straight: {card_name} High')
        return high_card


def check_straight(cards):
    card_dict = cards2dict(cards)
    straight, high = is_straight(card_dict)
    if straight:
        return straight, high
    else:
        return False, False

