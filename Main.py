#Main script from where the games are called

import DataBase
import Game1_Spaces
import Game2_Hangman
import Game3_Word
import Game4_Definition
import Game5_Match
import os

Dic = DataBase.open_DB()
executing = 1

while executing == 1:
    os.system("cls")
    print("Welcome to LANGUAGE PRACTICE!")
    print("\nManage the database:")
    print("1: add new words one by one")
    print("2: add new words from a file")
    print("3: show all the words in the database")
    print("4: empty the database")
    print("\nPlay games:")
    print("5: play to 'Spaces'")
    print("6: play to 'Hangman'")
    print("7: play to 'Word'")
    print("8: play to 'Definition'")
    print("9: play to 'Match'")
    print("\nOthers:")
    print("0: exit")

    response = input("\nWhat do you want to do? ")

    if response == "1":
        Dic = DataBase.add_single(Dic)
    elif response == "2":
        Dic = DataBase.add_from_file(Dic)
    elif response == "3":
        DataBase.show(Dic)
    elif response == "4":
        Dic = DataBase.clear(Dic)
    elif response == "5":
        Game1_Spaces.game(Dic)
    elif response == "6":
        Game2_Hangman.game(Dic)
    elif response == "7":
        Game3_Word.game(Dic)
    elif response == "8":
        Game4_Definition.game(Dic)
    elif response == "9":
        Game5_Match.game(Dic)
    else:
        print("\nOk, see you soon!\n")
        DataBase.close_DB(Dic)
        break


