import random
import os

def game(Dic):
    playing = 1
    while playing == 1:
        os.system("cls")
        words = []
        definitions = []

        while len(words) < 4:
            word, definition = random.choice(list(Dic.items()))
            if word not in words:
                words.append(word)
                definitions.append(definition)
        
        print("For the word '" + words[0] + "'\n")
        definitions_sorted = sorted(definitions)
        for number, element in enumerate(definitions_sorted):
            print(str(number + 1) + ": " + element)
        
        for attempt in range(3):
            response = int(input("\nWhat is the correct definition? ")) - 1
            if definitions_sorted[response] == definitions[0]:
                print("\nWell done! It's correct")
                break
            else:
                if attempt < 2:
                    print("\nNo! Sorry, try it another time, you have {} attempts left".format(2 - attempt))
                else:
                   print("\nNo! Sorry, the correct definition was '" + definitions[0] + "'")
         
        option = input("\nDo you want to play more? ")
        if option == "No" or option == "no":
            playing = 0