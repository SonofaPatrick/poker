from cardreader import *
from collections import Counter


def pair(rank_count):
    # takes count of cards and returns the pairs
    pairs = []
    for rank in rank_count:
        if rank_count[rank] > 1:
            pairs.append([rank for count in range(rank_count[rank])])
    return pairs


def pair_high(rank_count):
    # takes count of cards and returns the high card
    high_cards = []
    for rank in rank_count:
        if rank_count[rank] == 1:
            high_cards.append(rank)
    if high_cards:
        return max(high_cards)


def is_pair(rank, rank_count):
    # takes count of cards and returns boolean if pair, trips, or quads
    # TODO this function was updated to return a dict with key hierarchy, value: list of rank and high card
    high = pair_high(rank_count)
    if rank_count[rank] == 2:
        return {'hierarchy': 9, 'rank': rank, 'high': high}
        # one pair
    elif rank_count[rank] == 3:
        return {'hierarchy': 7, 'rank': rank, 'high': high}
        # three of a kind
    elif rank_count[rank] == 4:
        return {'hierarchy': 3, 'rank': rank, 'high': high}
        # four of a kind


def pair_type(rank_count):
    # TODO redo the func to account for updated is_pair
    # returns hand hierarchy, used for identifying the hand
    pairs = []
    for rank in rank_count:
        hierarchy = is_pair(rank, rank_count)
        if hierarchy:
            pairs.append(hierarchy)
    if pairs:
        return pairs


def one_pair(pairs):
    # TODO return a high card that is not the pair
    if pairs:
        if len(pairs) == 1:
            if pairs[0]['hierarchy'] == 9:
                return True, pairs[0]['rank']
        else:
            return False, False
    else:
        return False, False


def two_pair(pairs):
    # takes pairs, returns boolean and highest two pairs
    if pairs:
        if len(pairs) == 2:
            if pairs[0]['hierarchy'] == 9 and pairs[1]['hierarchy'] == 9:
                pair_mem = [pairs[0], pairs[1]]
                return True, pair_mem
            else:
                return False, None
        elif len(pairs) == 3:
            pair_mem = []
            for pair in pairs:
                if pair['hierarchy'] == 9:
                    pair_mem.append(pair['rank'])
            pair_mem.pop(pair_mem.index(min(pair_mem)))
            return True, pair_mem
        else:
            return False, None
    else:
        return False, None


def trips(pairs):
    pair_mem = []
    if pairs:
        for pair in pairs:
            if pair['hierarchy'] == 7:
                pair_mem.append(pair['rank'])
        if len(pair_mem) == 2:
            pair_mem.pop(pair_mem.index(min(pair_mem)))
        if pair_mem:
            return True, pair_mem
        else:
            return False, None
    else:
        return False, None


def quads(pairs):
    if pairs:
        for pair in pairs:
            if pair['hierarchy'] == 3:
                return True, pair['rank']
            else:
                return False, None
    else:
        return False, None


def check_full_house(pairs):
    one, trip, two_trip = False, False, False
    pair_mem = []
    trip_mem = []
    if not pairs:
        return False, None
    if len(pairs) > 1:

        for pair in pairs:
            if pair['hierarchy'] == 7:
                trip_mem.append(pair['rank'])
                trip = True

        for pair in pairs:
            if pair['hierarchy'] == 9:
                pair_mem.append(pair['rank'])
                one = True

        if len(trip_mem) == 2:
            two_trip = True

        if two_trip:
            trip_high = max(trip_mem)
            one_high = min(trip_mem)
            return True, {'trip': trip_high, 'one': one_high}
        elif one and trip:
            trip_high = max(trip_mem)
            one_high = max(pair_mem)
            return True, {'trip': trip_high, 'one': one_high}
        else:
            return False, None
    else:
        return False, None

