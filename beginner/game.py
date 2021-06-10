from beginner.deck import *
from beginner.players import *
import time
from beginner.pairtest import *
from beginner.flush import *
from beginner.straight import *
from beginner.cardreader import *
from beginner.straightflush import *
from highcard import high_cards
from hierdict import highest_hand


class Game:
    sb = 1
    bb = 2

    def __init__(self):
        self.round = True
        self.pot = 0
        self.total_bet = 0
        self.breaker = 0
        self.stage = 0

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
    while_break = 0
    while g.round:
        g.breaker = 0
        if while_break == 1:
            return
        for i in a:
            i.turn = True
            i.action_memory = True
            i_current = a.index(i) - 1
            i2 = a[i_current]
            if i.turn:

                if i.bet < i2.bet:
                    action = input(f'{i.name}, ${i2.bet - i.bet} to call\nCall, Raise, or Fold (c/r/f): ')

                    if action == 'f':
                        print(f'{i.name} folds')
                        g.update_bet(i.bet, i2.bet)
                        g.update_pot()
                        bet_memory()
                        print(f'{i2.name} takes ${g.pot} pot, profits ${i.bet_memory}')
                        i.chips -= i.bet
                        i2.chips -= i2.bet
                        i2.chips += g.pot
                        display_chips()
                        g.breaker = 4
                        return

                    elif action == 'c':
                        i.call_raise_fold(action, i.bet, i2.bet)
                        g.update_bet(i.bet, i2.bet)
                        print(f'Total bets: ${g.total_bet}')
                        if not i2.action_memory:
                            continue
                        elif i.bet == i2.bet:
                            i.chips -= i.bet
                            i2.chips -= i.bet
                            bet_memory()
                            break

                    else:
                        i.call_raise_fold(action, i.bet, i2.bet)
                    g.update_bet(i.bet, i2.bet)
                    print(f'Total bets: ${g.total_bet}')

                elif i.bet == i2.bet:
                    action = input(f'{i.name}\nCheck, Bet, or Fold (c/b/f): ')

                    if action == 'c':
                        print(f'{i.name} checks')
                        if not i2.action_memory:
                            continue
                        else:
                            i.chips -= i.bet
                            i2.chips -= i2.bet
                            bet_memory()
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
        if Player.player_list[0].position == 'Dealer':
            pass

        num_rounds = 0
        while g.round:
            p1.turn, p2.turn = False, False
            p1.action_memory, p2.action_memory = False, False
            g.breaker = 0
            num_rounds += 1
            print(f'\nRound: {num_rounds}')
            if num_rounds > 1:
                d = Deck()
                change_position()
                print(f'Cards in Deck: {len(d.current)}')
                d.shuffle()
                print('Shuffling...')
                time.sleep(3)
                d.deal_hands()
                p1.hand = d.two_hands[0]
                p2.hand = d.two_hands[1]
            for stage in range(5):
                stage += g.breaker
                if stage == 0:
                    print(f'{p2.chips}')
                    g.total_bet = 0
                    g.pot = 0
                    p1.bet, p2.bet = 0, 0

                    for i in a:
                        if i.position == 'Dealer':
                            i.bet = i.bet + Game.sb
                        else:
                            i.bet = i.bet + Game.bb
                    g.update_bet(p2.bet, p1.bet)

                    print('\n__Pre-flop__')
                    display_players()
                    print(f'\nPot: ${g.total_bet}')

                elif stage == 1:
                    p1.action_memory, p2.action_memory = False, False
                    p1.turn, p2.turn = False, False
                    d.deal_flop()
                    g.pot = g.total_bet
                    p1.bet, p2.bet = 0, 0

                    print('__Flop__')
                    print(d.flop)
                    g.update_bet(p1.bet, p2.bet)

                    display_players()
                    print(f'\nPot: ${g.pot}')

                elif stage == 2:
                    p1.action_memory, p2.action_memory = False, False
                    p1.turn, p2.turn = False, False
                    d.burn1_deal1()
                    g.update_pot()
                    p1.bet, p2.bet = 0, 0

                    print('__Turn__')
                    print(d.flop)
                    g.update_bet(p1.bet, p2.bet)

                    display_players()
                    print(f'\nPot: ${g.pot}')

                elif stage == 3:
                    p1.action_memory, p2.action_memory = False, False
                    p1.turn, p2.turn = False, False
                    d.burn1_deal1()
                    g.update_pot()
                    p1.bet, p2.bet = 0, 0

                    print('__River__')
                    print(d.flop)
                    g.update_bet(p1.bet, p2.bet)

                    display_players()
                    print(f'\nPot: ${g.pot}')

                elif stage > 3:
                    # d.flop = flop
                    # p1.hand, p2.hand
                    for player in Player.player_list:
                        player.flop_hand = play_copy(d.flop, player.hand)
                        player.rank_count = rank2count(player.flop_hand)
                        player.pairs = pair_type(player.rank_count)

                    for player in Player.player_list:

                        straight_flush = check_straight_flush(player.flop_hand)
                        four_of_a_kind, q_high = quads(player.pairs)
                        full_house, full_house_dict = check_full_house(player.pairs)
                        flush, suit, f_high, card_dict = check_flush(player.flop_hand)
                        straight, s_high = check_straight(player.flop_hand)
                        three_of_a_kind, trip_mem = trips(player.pairs)
                        two_pairs, two_mem = two_pair(player.pairs)
                        one_p, one_high = one_pair(player.pairs)

                        if straight_flush:
                            player.hierarchy[9] = True

                        elif four_of_a_kind:
                            player.hierarchy[8] = True

                        elif full_house:
                            player.hierarchy[7] = True

                        elif flush:
                            player.hierarchy[6] = True

                        elif straight:
                            player.hierarchy[5] = True

                        elif three_of_a_kind:
                            player.hierarchy[4] = True

                        elif two_pairs:
                            player.hierarchy[3] = True

                        elif one_p:
                            player.hierarchy[2] = True

                        player.highest_hand = highest_hand(player.hierarchy)

                    if p1.highest_hand > p2.highest_hand:
                        # TODO this chip update method is shoddy
                        p1.chips += g.pot
                        g.pot = 0
                    elif p2.highest_hand > p1.highest_hand:
                        p2.chips += g.pot
                        g.pot = 0
                    elif p1.highest_hand == p2.highest_hand:
                        if p1.highest_hand == 1:
                            # TODO need to cover all the high card draws
                            high_card = high_cards(p1.flop_hand, p2.flop_hand)
                            if high_card == 'p1':
                                p1.chips += g.pot
                                g.pot = 0
                            elif high_card == 'p2':
                                p2.chips += g.pot
                                g.pot = 0
                            elif high_card == 'draw':
                                pass
                            # TODO make a draw work
                    # TODO make a display for the winner
                    break
                game_round()
