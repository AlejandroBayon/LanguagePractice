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
        
        print("Words:\n")
        words_sorted = sorted(words)
        for number, element in enumerate(words_sorted):
            print(str(number + 1) + ": " + element)
        
        print("\nDefinitions:\n")
        definitions_sorted = sorted(definitions)
        for number, element in enumerate(definitions_sorted):
            print(str(number + 1) + ": " + element)


        for attempt in range(3):
            score = 0
            print()
            
            for question in range(4):
                response = int(input("What is the correct definition for the word " + str(question + 1) + "? ")) - 1
                selected_word = words_sorted[question]
                selected_definition = definitions_sorted[response]
                if words.index(selected_word) == definitions.index(selected_definition):
                    score += 1
            
            if score == 4:
                print("\nWell done! Everything is correct")
                break
            else:
                if attempt < 2:
                    print("\nNo! Sorry, you only got {} answers right. Try it another time, you have {} attempts left".format(score, 2 - attempt))
                else:
                   print("\nNo! Sorry, the correct answers were:\n")
                   for index in range(4):
                       print(words[index] + ": " + definitions[index])

        option = input("\nDo you want to play more? ")
        if option == "No" or option == "no":
            playing = 0