import time
import random

class Dice:
    __numbers = [1, 2, 3, 4, 5, 6]
    _your_wins = 0
    _computer_wins = 0

    def __init__(self, play):
        self.computer_dice_choice = random.choice(Dice.__numbers)
        self.your_dice_choice = random.choice(Dice.__numbers)
        self.play = play

    def game(self):
        print("Awaiting result from roll...")
        time.sleep(2)
        if self.computer_dice_choice > self.your_dice_choice:
            Dice._computer_wins += 1
            return f"\nThe computer dice is: {self.computer_dice_choice}\nYour dice is: {self.your_dice_choice}\nComputer Wins!\n"


        elif self.computer_dice_choice < self.your_dice_choice:
            Dice._your_wins += 1
            return f"\nThe computer dice is: {self.computer_dice_choice}\nYour dice is: {self.your_dice_choice}\nYou Win!\n"

        else:
            return f"\nThe computer dice is:  {self.computer_dice_choice}\nYour dice is: {self.your_dice_choice}\nNobody wins a draw!\n"


    def __repr__(self):
        if self.play == "yes":
            return self.game()
        return f"The game finished the result is:\nYour Wins: {str(Dice._your_wins)}\nComputer Wins: {str(Dice._computer_wins)}"

dice = Dice

start_game = input("Welcome Dice game \n\nDo you wanna start the game: (yes or no)\n").lower()
while "yes" != start_game != "no":
    print("Please write correct input")
    start_game = input("Do you wanna start the game: (yes or no)\n").lower()
else:
    while start_game != "no":
        if "no" != start_game != "yes":
            print("Please write correct input")
            start_game = input("Do you wanna roll again?\n")
            continue
        print(dice(start_game))
        start_game = input("Do you wanna roll again?\n")
    print(dice(start_game))