import random


SIX_HANDS = []
PLAYER_LIST = []
if len(PLAYER_LIST) > 6:
    PLAYER_LIST.pop()


class Deck(object):

    def __init__(self,):
        self.two_hands = []
        self.current = ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ac',
                        '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks', 'As',
                        '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd', 'Ad',
                        '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh', 'Ah']
        self.hand = []
        self.flop = []
        self.pile = []

    def shuffle(self):
        # adding the pile back to the deck
        self.current.extend(self.two_hands)
        self.current.extend(self.flop)
        self.current.extend(self.pile)
        # TODO: make sure to actually understand what this does
        # shuffling the created deck
        # range(start, stop, step)
        # pretty cool shuffle function from stackoverflow
        for i in range(len(self.current)-1, 0, -1):
            r = random.randint(0, i)
            self.current[i], self.current[r] = self.current[r], self.current[i]

    def deal_hands(self):
        # TODO: update this function to simulate dealing one round of cards to each player, then a second round
        # drawing a card from the created deck
        for i in range(2):
            # this loop creates six hands, two cards each, by drawing them from the deck
            for a in range(2):
                self.hand.append(self.current.pop())
            self.two_hands.append(self.hand)
            self.hand = []

    def deal_flop(self):
        # burn one card
        self.pile.append(self.current.pop())
        for b in range(3):
            # deal three cards to the flop
            self.flop.append(self.current.pop())

    def burn1_deal1(self):
        # for the turn and river cards
        self.pile.append(self.current.pop())
        self.flop.append(self.current.pop())


def my_hand(players, hands):
    # input player name, output their hand
    # the easiest way to do this:
    # link the player and hand by their shared indexes in PLAYER_LIST and SIX_HANDS
    name = input('Who are you?')
    a = players.index(name)
    print(f'Hello {name}, your hand is {hands[a]}')


if __name__ == "__main__":
    # TODO: i left off here. trying to initialize the game. will still need to deal flop cards and implement chips.
    pass

# poop
