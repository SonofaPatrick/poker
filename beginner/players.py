

class Player:
    player_list = []

    def __init__(self, name, position, hand, chips):
        # create an object for each player. append their name to the player list.
        self.name = name
        self.chips = int(chips)
        self.hand = hand
        self.position = position
        self.turn = False

        self.bet = 0
        self.bet_current = 0
        self.bet_memory = 0
        self.action_memory = False

        self.flop_hand = None
        self.rank_count = None
        self.pairs = None
        self.hierarchy = {10: False, 9: False, 8: False, 7: False, 6: False,
                          5: False, 4: False, 3: False, 2: False, 1: True}
        self.highest_hand = None

        Player.player_list.append(self)

    def change_position(self):
        if self.position == 'Dealer':
            self.position = 'Big Blind'
        else:
            self.position = 'Dealer'

    def call_raise_fold(self, action, my_bet, their_bet):
        # TODO create fold and check function
        if action == 'c':
            called_chips = their_bet - my_bet
            self.bet = self.bet + called_chips
            # self.chips = self.chips - called_chips
            print(f'{self.name} called')
        elif action == 'r':
            self.bet_current = int(input(f'{self.name}\nEnter raise: '))
            self.bet = self.bet + self.bet_current
            # self.chips = self.chips - self.bet_current
            print(f'{self.name} raises ${self.bet_current}')
        elif action == 'f':
            pass
            # fold()
        else:
            print('Incorrect input. Try (c/r/f)')

    def check_bet_fold(self, action):
        if action == 'c':
            pass
            # check()
        elif action == 'b':
            self.bet_current = int(input(f'{self.name}\nEnter bet: '))
            self.bet = self.bet + self.bet_current
            # self.chips = self.chips - self.bet_current
            print(f'{self.name} bets ${self.bet_current}')
        elif action == 'f':
            pass
            # fold()
        else:
            print('Incorrect input. Try (c/b/f)')


def bet_memory():
    for player in Player.player_list:
        player.bet_memory += player.bet


def turn_order(player):
    if player.position == 'Dealer':
        player.turn = True
    else:
        player.turn = False


def change_position():
    for player in Player.player_list:
        if player.position == 'Dealer':
            player.position = 'Big Blind'
        elif player.position == 'Big Blind':
            player.position = 'Dealer'
        print(f'{player.name} is {player.position}')


def display_chips():
    for player in Player.player_list:
        print(f"{player.name}'s chips: ${player.chips}")


def display_players():
    for player in Player.player_list:
        print(f"\n{player.name}\n{str(player.hand)}\n{player.position}: ${player.bet}\n${player.chips - player.bet}")


def player_names():
    names = []
    chips = []
    for a in range(2):
        b = input('Name:')
        c = input('Starting Stack:')
        names.append(b)
        chips.append(c)
    return names, chips


def player_chips(chips):
    # c = input('Starting Chips:')
    return chips


def player_positions():
    p = ['Dealer', 'Big Blind']
    return p


def create_players():
    pass


if __name__ == "__main__":
    names = player_names()
    h = [['Ks', 'Kc'], ['Qs', 'Qc']]
    c = player_chips(1000)
    p1 = Player(names[0], 'Dealer', h[0], c)
    p2 = Player(names[1], 'Big Blind', h[1], c)
    print(p1.name, p1.position, p1.hand, p1.chips)
    print(Player.player_list)
