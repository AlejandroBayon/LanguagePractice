import random

def game(Dic):
    playing = 1
    while playing == 1:
        word, definition = random.choice(list(Dic.items()))
        first_letter = word[0]
        spaces = len(word) - 2
        last_letter = word[-1]

        print(definition)
        print(first_letter + " " + "_ " * spaces + last_letter)

        for attempt in range(3):
            response = input("What is the correct word? ")
            if response == word:
                print("Well done! It's correct")
                break
            else:
                if attempt < 2:
                    print("Try it another time, you have {} attempts left".format(2 - attempt))
                else:
                   print("Sorry, the correct word was " + word)
        option = input("Do you want to play more? Yes or No: ")
        if option == "No":
            playing = 0