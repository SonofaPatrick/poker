
hierarchy_dict = {10: False, 9: False, 8: True, 7: False, 6: False, 5: True, 4: False, 3: False, 2: False, 1: True}


def highest_hand(hierarchy_dict):
    for hand in hierarchy_dict:
        if hierarchy_dict[hand] is True:
            return hand

# 10 - Royal Flush
# 9  - Straight Flush
# 8  - Four of a Kind
# 7  - Full House
# 6  - Flush
# 5  - Straight
# 4  - Three of a Kind
# 3  - Two Pair
# 2  - One Pair
# 1  - High Card

