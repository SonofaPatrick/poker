import random
import collections

# sdfk02k403fk2
#asdasd

SIX_HANDS = []
PLAYER_LIST = []
if len(PLAYER_LIST) > 6:
    PLAYER_LIST.pop()


class Deck(object):
    initial_deck = ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ac',
                    '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks', 'As',
                    '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd', 'Ad',
                    '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh', 'Ah']

    def __init__(self, deck):
        self.six_hands =[]
        self.current = deck
        self.hand = []
        self.flop = []

    def shuffle(self):
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
        for i in range(6):
            # this loop creates six hands, two cards each, by drawing them from the deck
            for a in range(2):
                self.hand.append(self.current.pop())
            SIX_HANDS.append(self.hand)
            self.hand = []

    def deal_flop(self):
        # burn one card
        self.current.pop()
        for b in range(3):
            # deal three cards to the flop
            self.flop.append(self.current.pop())

    def burn1_deal1(self):
        # for the turn and river cards
        self.current.pop()
        self.flop.append(self.current.pop())


class PlayerList:
    def __init__(self):
        self.player_list = []

    def player(self, name):
        for i in range(6):
            names = input('Name:')


class Player(PlayerList):
    # TODO work on this superclass.
    def __init__(self, name):
        # create an object for each player. append their name to the player list.
        self.name = name
        # self.hand = hand
        PLAYER_LIST.append(self.name)

    def new_hand(self):
        pass


class Position:
    def __init__(self,):
        self.position = ['Button', 'Small Blind', 'Big Blind', 'Under the Gun', 'Hijack', 'Cutoff']

    def update(self):
        self.position = self.position[1:] + self.position[:1]


def my_hand(players, hands):
    # input player name, output their hand
    # the easiest way to do this:
    # link the player and hand by their shared indexes in PLAYER_LIST and SIX_HANDS
    name = input('Who are you?')
    a = players.index(name)
    print(f'Hello {name}, your hand is {hands[a]}')


def players():
    # creating the list of players through the Player class
    for a in range(6):
        b = input('Name:')
        Player(b)


if __name__ == "__main__":
    # TODO: i left off here. trying to initialize the game. will still need to deal flop cards and implement chips.
    d = Deck(Deck.initial_deck)
    d.shuffle()
    d.shuffle()

    players()
    p = Position(PLAYER_LIST)

    d.deal_hands()

    my_hand(PLAYER_LIST, SIX_HANDS)
    print(SIX_HANDS)



def next_turn():
    # after the first turn ends, start a new one
    # ignore this function for now
    n = Deck(Deck.initial_deck)
    n.shuffle()
    n.shuffle()
    # shuffle that bitch twice
    n.deal_hands()





