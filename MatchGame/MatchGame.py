import random


class MatchGame:

    def __init__(self,cards):
        self.cards = list(cards)
        self.row_length = len(self.cards)
        self.show = []

    def set_cards(self):
        self.cards = self.cards * 2
        random.shuffle(self.cards)
        self.show = [str(num) for num in range(1,len(self.cards) + 1)]

    def display(self):
        first_row = self.show[ :self.row_length]
        second_row = self.show[self.row_length: ]
        print(f"{'  '.join(first_row)}\n{'  '.join(second_row)}")

    def play(self,pick1,pick2):
        card = None
        if self.cards[pick1 - 1] == self.cards[pick2 - 1]:
            card = self.cards[pick1 - 1]
            self.show[pick1 - 1] = self.show[pick2 - 1] = self.cards[pick1 - 1]
        return card 

    def finish(self):
        if all([x.isalpha() for x in self.show]):
            return True
        else:
            return False


def main():
    
    cards = {'monster', 'apple', 'dog', 'balloon', 'gun'}
    game = MatchGame(cards)
    game.set_cards()
    show_card = []
    print("Match Card Game")
    finish = False

    while finish == False:
        game.display()
        show_card = game.show
        enter = input("Choose 2 cards seprated by comma: ")
        enter = enter.split(',')
        if (len(enter) != 2 
            or enter[0] == enter[1]
            or all([x in show_card for x in enter]) == False):
            print("Invalid Input")
            continue
        pick1 = int(enter[0])
        pick2 = int(enter[1])
        card = game.play(pick1, pick2)
        if card == None:
            print("Sorry, you didn't guess right, try again.")
            continue
        print(f"You got {card}")
        finish = game.finish()
    else:
        print("Congratulation! You got all of them")


main()