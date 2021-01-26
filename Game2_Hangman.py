import random
import os
import time

def game(Dic):
    playing = 1
    while playing == 1:
        word, definition = random.choice(list(Dic.items()))
        user_letters = []
        lifes = 5

        while lifes > 0:
            os.system("cls")
            print("Guess the word with this definition: '" + definition + "'\n")
            guess_word = ""
            letters_said = ""
            for letter in word:
                if letter in user_letters:
                    guess_word = guess_word + letter + " "
                else:
                    guess_word = guess_word + "_ "
            print(guess_word)
            for user_letter in user_letters:
                letters_said = letters_said + user_letter + " "
            print("\nYou have said the following letters: " + letters_said)
            response = input("\nSay a letter, or the word if you know it: ")
            message = ""
            if response == word:
                print("\nWell done! It's correct\n")
                break
            elif response in user_letters:
                message = message + "\nThis letter has been said before. "
            elif response not in word:
                message = message + "\nSorry, this letter isn't in the word. "
                user_letters.append(response)
                lifes -= 1
            else:
                message = message + "\nWell done, this letter is in the word. "
                user_letters.append(response)
            if lifes == 0:
                message = message + "You don't have more lifes. The correct word was '" + word + "'\n"
            else:
                message = message + "You have " + str(lifes) + " lifes left\n"
            print(message)
            if lifes > 0:
                time.sleep(4)
                
        option = input("Do you want to play more? ")
        if option == "No" or option == "no":
            playing = 0