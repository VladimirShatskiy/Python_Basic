import random


class Card:
    def __init__(self, rang, suit, hand=False):
        self.rang = rang
        self.suit = suit
        self.on_hand = hand

    def prn(self):
        print(f'{self.rang} {self.suit}')


class Deck:

    def __init__(self):
        self.card = [Card(card_rang[i], card_suit[x]) for i in range(len(card_rang)) for x in range(len(card_suit))]

    def prn(self):
        for i in self.card:
            print(f'"{i.rang} {i.suit}"', end='')


class Player:

    def __init__(self, name='Компьютер'):
        self.name = name
        self.cards = []
        self.score = 0

    def card_add(self, deck):
        card = card_choice(deck)
        self.cards.append(card)
        self.score += card_score(card, self.score)

    def prn(self):
        print(f'\n{self.name} {self.score}')
        for item in self.cards:
            item.prn()


def card_choice(deck):
    while True:
        card_n = random.randint(0, len(deck) - 1)
        if not deck[card_n].on_hand:
            deck[card_n].on_hand = True
            return deck[card_n]


def card_score(card, score):
    if type(card.rang) == int:
        return card.rang
    elif card.rang != 'A':
        return 10
    else:
        if score < 21:
            return 11
        else:
            return 1


card_rang = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
card_suit = ['Diamonds', 'Hearts', 'Spades', 'Clubs']

game_deck = Deck()
gamer1 = Player()
gamer2 = Player('Владимир')

# раздача карт по 2
for _ in range(2):
    gamer1.card_add(game_deck.card)
    gamer2.card_add(game_deck.card)

flag = True
while flag:
    print(f'Раздали карт {len(gamer2.cards)}, у тебя {gamer2.score} очков, карты на руках')
    for item in gamer2.cards:
        item.prn()

    if input('\nПродолжить игру y/n ?').lower() == 'y':
        gamer1.card_add(game_deck.card)
        gamer2.card_add(game_deck.card)
    else:
        flag = False

    if gamer2.score > 21 or gamer1.score > 21:
        flag = False
    elif gamer2.score == 21:
        print('Очко !')
        flag = False
info ='Победителей нет'
win_iq = '!!!Победил Компьютер !!!'
win_pl = '!!!Победил Игрок !!!'
if gamer2.score > gamer1.score:
    if gamer2.score < 21:
        info =win_pl
    else:
        if gamer1.score < 21:
            info = win_iq

if gamer2.score < gamer1.score:
    if gamer1.score < 21:
        info = win_iq
    else:
        if gamer2.score < 21:
            info =win_pl

if gamer2.score == gamer1.score and gamer2.score < 21:
    info = "Ничья"

print(f'\n {info}')
gamer2.prn()
gamer1.prn()