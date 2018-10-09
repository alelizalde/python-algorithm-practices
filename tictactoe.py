"""
Tic tac toe
"""

import os


class Game:
    """
    Class game with initial parameters
    """
    def __init__(self):
        self.board = {1: " ", 2: " ", 3: " ",
                      4: " ", 5: " ", 6: " ",
                      7: " ", 8: " ", 9: " "}

        self.mark = "X"
        self.turns = 9

    def __str__(self):
        return "game is active"

    @staticmethod
    def end_game():
        """
        Example method
        """
        print(f"Game over")
        exit(0)


def check_winner(current_mark, lboard):
    """
    Check for the winner
    """
    return ((lboard[1] == lboard[2] == lboard[3] == current_mark) or
            (lboard[4] == lboard[5] == lboard[6] == current_mark) or
            (lboard[7] == lboard[8] == lboard[9] == current_mark) or
            (lboard[1] == lboard[4] == lboard[7] == current_mark) or
            (lboard[2] == lboard[5] == lboard[8] == current_mark) or
            (lboard[3] == lboard[6] == lboard[9] == current_mark) or
            (lboard[1] == lboard[5] == lboard[9] == current_mark) or
            (lboard[3] == lboard[5] == lboard[7] == current_mark))


def print_board(lboard):
    """
    Print board
    """
    os.system('clear')
    print("hit 'q' to quit")
    print(lboard[1] + "|" + lboard[2] + "|" + lboard[3])
    print(lboard[4] + "|" + lboard[5] + "|" + lboard[6])
    print(lboard[7] + "|" + lboard[8] + "|" + lboard[9])


def new_game(game):
    """
    create new game
    """
    game.turns = 9
    del game.board
    game.board = {1: " ", 2: " ", 3: " ",
                  4: " ", 5: " ", 6: " ",
                  7: " ", 8: " ", 9: " "}


def main():
    """
    main function
    """

    game = Game()

    print_board(game.board)
    while True:

        if game.turns == 0:
            print("There is no winner")
            play_again = input("Play again? (y/n)")
            if play_again.lower() == "n":
                break
            else:
                new_game(game)
                print_board(game.board)

        position = input()

        if position.lower() == "q":
            break

        try:
            position = int(position)
        except ValueError:
            pass

        if position in game.board and game.board[position] == " ":
            game.turns -= 1
            if game.mark == "X":
                game.mark = "O"
            else:
                game.mark = "X"
            game.board[position] = game.mark
            print_board(game.board)
            if check_winner(game.mark, game.board):
                print(f"{game.mark} is the winner")
                play_again = input("Play again? (y/n)")
                if play_again.lower() == "n" or play_again.lower() == "q":
                    break
                else:
                    new_game(game)
                    print_board(game.board)


if __name__ == '__main__':
    main()
