

def identify(poker_hand):
    hierarchy = []
    winner = 'High Card'
    for pairs in poker_hand:
        if len(pairs) == 2:
            hierarchy.append(9)
            # one pair
        elif len(pairs) == 3:
            hierarchy.append(7)
            # trips
        elif len(pairs) == 4:
            hierarchy.append(3)
            # quads
    if not hierarchy:
        winner = 'High Card'
        return winner
    if len(hierarchy) == 2:
        if hierarchy[0] and hierarchy[1] == 9:
            winner = 'Two Pair'
        if hierarchy[0] or hierarchy[1] == 7:
            winner = 'Three of a Kind'
        if hierarchy[0] or hierarchy[1] == 9:
            winner = 'One Pair'
            if hierarchy[0] or hierarchy[1] == 7:
                winner = 'Full House'
            elif hierarchy[0] or hierarchy[1] == 3:
                winner = 'Four of a Kind'
    elif hierarchy[0] == 9:
        winner = 'Two Pair'
    elif hierarchy[0] == 7:
        winner = 'Three of a Kind'
    elif hierarchy[0] == 3:
        winner = 'Four of a Kind'
    return winner
