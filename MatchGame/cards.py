class Cards:
    """
    This class represent a set of cards, it has pictures and position.
    The flip method can get a card's picture by its position.
    The layout method return a list for printing to the console.
    """

    def __init__(self, pics, positions):
        self.cards = []
        for pic, position in zip(pics, positions):
            self.cards.append([pic, position, False])

    def __iter__(self):
        yield from self.cards

    def flip(self, position):
        for card in self.cards:
            if card[1] == position:
                return card[0]

    def layout(self):
        self.layput_list = []
        for card in self.cards:
            value = card[0] if card[2] == True else ' '
            self.layput_list.append(value)
        return self.layput_list
    
