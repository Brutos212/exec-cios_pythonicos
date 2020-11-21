import os
import time
import random
import keyboard


def populator():
    # Generates a list with number 1 to 90 in random order
    numbers = []
    while True:
        if len(numbers) == 89:
            # Breaks loop if len == 89
            # remember list index start counting at 0
            break
        else:
            # Generate a random number
            num = random.randint(1, 90)
            for i in numbers:
                # Iterate through the numbers - list variable
                if i == num:
                    # If generated number already in the list
                    # It runs the script again
                    continue
            # If num not in numbers, add it
            numbers.append(num)
            # Returns a generator object
            yield num


def game():
    # Starts the game
    # Cleans the terminal
    os.system("cls")
    print("[ - BANKO GAME ]\n"
          "[ROLL]   > Press Space\n"
          "[BINGO]  > Press Enter\n"
          "[EXIT]   > Press Escape\n")
    # Creates a new instance of populator function
    # This result in a new list of random numbers 1-90

    numbers = populator()
    while True:
        # Our controls, we only accept key presses
        if keyboard.is_pressed("space"):
            print(next(numbers))
            time.sleep(1)
        elif keyboard.is_pressed("enter"):
            return game()
        elif keyboard.is_pressed("escape"):
            break

    if __name__ == '__main__':
        game()
