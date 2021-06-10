from collections import Counter
from cardreader import *


def suit_translate(suit):
    if suit == 'c':
        return 'Clubs'
    elif suit == 's':
        return 'Spades'
    elif suit == 'h':
        return 'Hearts'
    elif suit == 'd':
        return 'Diamonds'


def flush_high(suit, card_dict):
    ranks = []
    for card in card_dict:
        if suit == card['suit']:
            ranks.append(card['rank'])
    return max(ranks)


def is_flush(cards):
    test_suits = ['h', 'd', 's', 'c']
    card_dict = cards2dict(cards)
    for suit in test_suits:
        suits = []
        for card in card_dict:
            if suit == card['suit']:
                suits.append(True)
        if len(suits) >= 5:
            return True, suit, card_dict
    else:
        return False, False, False


def check_flush(cards):
    # checks if the input cards make a flush, returns flush and high card
    flush, suit, card_dict = is_flush(cards)
    if flush:
        high_card = flush_high(suit, card_dict)
        print(f'Flush: {suit_translate(suit)}, {rank2face(high_card)} High')
        return flush, suit, high_card, card_dict
    else:
        return False, False, False, False


