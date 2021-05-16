from main import *
from collections import defaultdict

# players()
# next_turn()
# my_hand(PLAYER_LIST, SIX_HANDS)
#
# my_hand(PLAYER_LIST, SIX_HANDS)
# my_hand(PLAYER_LIST, SIX_HANDS)
# my_hand(PLAYER_LIST, SIX_HANDS)

x = 1
a = x+1
print(x)
print(a)

b = [1,2,3,4]
a = b
a.pop()
print(b)
print(a) # a = [1,2,3] b = [1,2,3,4]

p = Position()
print(p.position)
p.update()
print(p.position)
