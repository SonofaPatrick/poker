from beginner.deck import *
from beginner.players import *
import time

class Game:
    sb = 1
    bb = 2

    def __init__(self):
        self.round = True
        self.pot = 0
        self.total_bet = 0
        self.breaker = 0

    def update_bet(self, bet1, bet2):
        self.total_bet = bet1 + bet2

    def update_pot(self):
        self.pot = self.pot + self.total_bet

    def reset(self):
        self.pot = 0
        self.total_bet = 0
        self.breaker = 0

    def round_end(self):
        self.round = False


def set_blinds(small_blind, big_blind):
    Game.sb = small_blind
    Game.bb = big_blind


def game_round():
    while g.round:
        g.breaker = 0
        for i in a:
            i.turn = True
            i_current = a.index(i) - 1
            i2 = a[i_current]

            if i.turn:

                if i.bet < i2.bet:
                    action = input(f'{i.name}, ${i2.bet - i.bet} to call\nCall, Raise, or Fold (c/r/f): ')

                    if action == 'f':
                        print(f'{i.name} folds')
                        i2.chips += i2.bet - i.bet
                        g.pot += g.total_bet - (i2.bet - i.bet)
                        print(f'{i2.name} wins ${g.pot}')
                        i2.chips += g.pot
                        g.breaker = 4
                        break

                    elif action == 'c':
                        i.call_raise_fold(action, i.bet, i2.bet)
                        g.update_bet(i.bet, i2.bet)
                        print(f'Total bets: ${g.total_bet}')
                        if not i2.turn:
                            continue
                        elif i.bet == i2.bet:
                            break

                    else:
                        i.call_raise_fold(action, i.bet, i2.bet)
                    g.update_bet(i.bet, i2.bet)
                    print(f'Total bets: ${g.total_bet}')

                elif i.bet == i2.bet:
                    action = input(f'{i.name}\nCheck, Bet, or Fold (c/b/f): ')

                    if action == 'c':
                        print(f'{i.name} checks')
                        if not i2.turn:
                            continue
                        else:
                            break
                    # TODO update this fold statement
                    elif action == 'f':
                        print(f'{i.name} folds')
                        i2.chips = i2.chips + g.pot
                        break

                    else:
                        i.check_bet_fold(action)
                    g.update_bet(i.bet, i2.bet)
                    print(f'Total bets: ${g.total_bet}')

            # i.turn = False
        else:
            continue
        break


if __name__ == '__main__':
    g = Game()
    # creating Game
    d = Deck()
    # creating Deck
    d.shuffle()
    d.deal_hands()
    # dealing two hands
    h = d.two_hands
    n, c = player_names()
    # n = input('Name')
    # c = input('Starting Stack:')
    p = player_positions()
    # creating Player 1, and Player 2, with name, position, hand, and chip count
    p1 = Player(n[0], p[0], h[0], c[0])
    p2 = Player(n[1], p[1], h[1], c[1])

    a = Player.player_list
    # highly important variable:
    # a = a list of two Player objects.
    print(f'\n{p1.name} buys in for ${a[0].chips}')
    print(f'{p2.name} buys in for ${a[1].chips}')

    # TODO fix the pre-flop fold
    # TODO work on the game loop
    while g.round:
        num_rounds = 0
        while g.round:
            g.breaker = 0
            num_rounds += 1
            print(num_rounds)
            if num_rounds > 1:
                d = Deck()
                print(f'Cards in Deck: {len(d.current)}')
                d.shuffle()
                print('Shuffling...')
                time.sleep(3)
                d.deal_hands()
                p1.hand = d.two_hands[0]
                p2.hand = d.two_hands[1]
            for stage in range(4):
                stage += g.breaker
                if stage == 0:
                    g.pot = 0
                    p1.bet, p2.bet = 0, 0
                    for i in a:
                        if i.position == 'Dealer':
                            i.chips = i.chips - Game.sb
                            i.bet = i.bet + Game.sb
                        else:
                            i.chips = i.chips - Game.bb
                            i.bet = i.bet + Game.bb
                    g.update_bet(p2.bet, p1.bet)
                    g.update_pot()
                    print('\n__Pre-flop__')
                    print(f'\n{p1.name}\n{str(p1.hand)}\n{p1.position}: ${p1.bet}\n${p1.chips}')
                    print(f'\n{p2.name}\n{str(p2.hand)}\n{p2.position}: ${p2.bet}\n${p2.chips}')
                    print(f'\nPot: ${g.pot}')
                elif stage == 1:
                    p1.turn, p2.turn = False, False
                    d.deal_flop()
                    g.pot = g.total_bet
                    p1.bet, p2.bet = 0, 0
                    print('__Flop__')
                    print(d.flop)
                    g.update_bet(p1.bet, p2.bet)
                    print(f'\n{p1.name}\n{str(p1.hand)}\n{p1.position}: ${p1.bet}\n${p1.chips}')
                    print(f'\n{p2.name}\n{str(p2.hand)}\n{p2.position}: ${p2.bet}\n${p2.chips}')
                    print(f'\nPot: ${g.pot}')
                    x = input('Start post-flop')
                elif stage == 2:
                    p1.turn, p2.turn = False, False
                    d.burn1_deal1()
                    g.update_pot()
                    p1.bet, p2.bet = 0, 0
                    print('__Turn__')
                    print(d.flop)
                    g.update_bet(p1.bet, p2.bet)
                    print(f'\n{p1.name}\n{str(p1.hand)}\n{p1.position}: ${p1.bet}\n${p1.chips}')
                    print(f'\n{p2.name}\n{str(p2.hand)}\n{p2.position}: ${p2.bet}\n${p2.chips}')
                    print(f'\nPot: ${g.pot}')
                    x = input('Start turn')
                elif stage == 3:
                    p1.turn, p2.turn = False, False
                    d.burn1_deal1()
                    g.update_pot()
                    p1.bet, p2.bet = 0, 0
                    print('__River__')
                    print(d.flop)
                    g.update_bet(p1.bet, p2.bet)
                    print(f'\n{p1.name}\n{str(p1.hand)}\n{p1.position}: ${p1.bet}\n${p1.chips}')
                    print(f'\n{p2.name}\n{str(p2.hand)}\n{p2.position}: ${p2.bet}\n${p2.chips}')
                    print(f'\nPot: ${g.pot}')
                    x = input('Start River')
                elif stage > 3:
                    break
                game_round()
