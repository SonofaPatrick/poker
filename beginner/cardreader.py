from collections import Counter


def cards2dict(cards):
    # take list of cards, return dict list of cards with ranks and suits
    dict_list = []
    for card in cards:
        card_dict = {'rank': card_rank(card), 'suit': card_suit(card)}
        dict_list.append(card_dict)
    return dict_list


def dict2cards(card_dict):
    card_list = []
    for card in card_dict:
        card_list.append(rank2face(card['rank']) + card['suit'])
    return card_list


def dict2card(card):
    c = rank2face(card['rank']) + card['suit']
    return c


def cards2rank(cards):
    # input list of cards and returns the list of ranks
    card_dict = cards2dict(cards)
    ranks = []
    for card in card_dict:
        ranks.append(card['rank'])
    return ranks


def rank2count(cards):
    # input list of cards and returns count of cards
    ranks = cards2rank(cards)
    rank_count = dict(Counter(ranks))
    return rank_count


def play_copy(flop, hand):
    flop_copy = flop.copy() + hand.copy()
    return flop_copy


def card_rank(card):
    if card[0] == '1':
        return 10
    elif card[0] == 'J':
        return 11
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'K':
        return 13
    elif card[0] == 'A':
        return 14
    else:
        return int(card[0])


def rank2face(rank):
    # takes the rank of a face card and gives the name
    if rank == 11:
        return 'J'
    elif rank == 12:
        return 'Q'
    elif rank == 13:
        return 'K'
    elif rank == 14:
        return 'A'
    else:
        return str(rank)


def card_suit(card):
    if card[0] == '1':
        return card[2]
    else:
        return card[1]



