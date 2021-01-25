import random

def game(Dic):
    playing = 1
    while playing == 1:
        word, definition = random.choice(list(Dic.items()))
        user_letters = []
        lifes = 5

        print("\nGuess the word with this definition: '" + definition + "'\n")
        while lifes > 0:
            guess_word = ""
            for letter in word:
                if letter in user_letters:
                    guess_word = guess_word + letter + " "
                else:
                    guess_word = guess_word + "_ "
            print(guess_word)
            response = input("\nSay a letter or the word if you know it: ")
            if response == word:
                print("\nWell done! It's correct\n")
                break
            elif response in user_letters:
                print("\nThis letter has been said before")
            elif response not in word:
                print("\nSorry, this letter isn't in the word")
                lifes -= 1
            else:
                print("\nWell done, this letter is in the word")
                user_letters.append(response)
            if lifes == 0:
                print("\nYou don't have more lifes. The correct word was '" + word + "'\n")
            else:
                print("\nYou have " + str(lifes) + " lifes left\n")
                
        option = input("Do you want to play more? ")
        if option == "No" or option == "no":
            playing = 0