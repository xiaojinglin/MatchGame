from cards import Cards
from prettytable import PrettyTable
import random


class Game:
    """
    This class present a game, it has a set of cards, and a table to print the cards.
    The shuffle method shuffle the cards before the new game start.
    The display method display the cards table, the cell is blank untill you match 2
    position
    The play method get two position and check whether their pictures are match
    The finish method check whether the game is finish.
    """

    pics = ['apple', 'chicken', 'dog', 'gun', 'heart', 'ball', 'pan', 'book'] * 2
    positions = []
    for i in range(1,5):
        for j in ['A', 'B', 'C', 'D']:
            positions.append(j + str(i))

    def __init__(self):
        self.cards = Cards(self.pics, self.positions)
        self.table = PrettyTable([' ', 'A', 'B', 'C', 'D'])
        self.display_list = []
        
    def shuffle(self):
       random.shuffle(self.pics)
       self.cards = Cards(self.pics, self.positions)

    def display(self):
        self.display_list = self.cards.layout()
        self.table.clear_rows()
        for i in range(4):
            row = [i + 1]
            row.extend(self.display_list[i*4: i*4+4])            
            self.table.add_row(row)
        print(self.table)

    def play(self,position1,position2):
        pic1 = self.cards.flip(position1)        
        pic2 = self.cards.flip(position2)
        if pic1 == pic2:
            for card in self.cards:
                if card[0] == pic1:
                    card[2] =True
            return [pic1]
        else:
            return [pic1, pic2]

    def finish(self):
        self.is_finish = all([card[2] for card in self.cards])
        return self.is_finish