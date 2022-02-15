from game import Game


def get_input(cards, position_success):
    """
    This function get the input from console and check whether the input is valid
    """
    while True:
        enter = input().upper()
        if enter not in Game.positions:
            enter = print("Invalid Input, try again: ")
            continue
        elif enter in position_success:
            print("You should choose an unknow card, try again: ")
            continue
        else:
            return enter


def main():
    """
    Main function start the game, keep the game going until it is finish.
    """
    game = Game()
    cards = game.cards
    game.shuffle()
    position_success = []
    is_finish = False
    while is_finish == False:
        game.display()
        print("Choose your first card(A1-A4,B1-B4,C1-C4,D1-D4): ")
        position1 = get_input(cards, position_success)
        print("Choose your second card(A1-A4,B1-B4,C1-C4,D1-D4): ")
        position2 = get_input(cards, position_success)
        if position1 == position2:
            print("You should choose two different position")
            continue
        result = game.play(position1, position2)
        if len(result) == 1:
            print(f"{position1}: {result[0]}, {position2}: {result[0]}, you got it!")
            position_success += [position1, position2]
            is_finish = game.finish()
        else:
            print(f"{position1}: {result[0]}, {position2}: {result[1]}, no match!")
    else:
        print("Congratuation! You did it")


main()