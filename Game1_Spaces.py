import random
import os

def game(Dic):
    playing = 1
    while playing == 1:
        os.system("cls")
        word, definition = random.choice(list(Dic.items()))
        first_letter = word[0]
        spaces = len(word) - 2
        last_letter = word[-1]

        print("The word definition is: '" + definition + "'\n")
        print(first_letter + " " + "_ " * spaces + last_letter)

        for attempt in range(3):
            response = input("\nWhat is the correct word? ")
            if response == word:
                print("\nWell done! It's correct")
                break
            else:
                if attempt < 2:
                    print("\nNo! Sorry, try it another time, you have {} attempts left".format(2 - attempt))
                else:
                   print("\nNo! Sorry, the correct word was " + word)
        option = input("\nDo you want to play more? ")
        if option == "No" or option == "no":
            playing = 0