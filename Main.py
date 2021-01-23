#Main script from where the games are called

import DataBase
import Game1_Spaces

Dic = DataBase.open_DB()
executing = 1
print("\nWelcome to LANGUAGE PRACTICE!")

while executing == 1:
    print("\nWhat do you want to do?")
    print("\nAdd new words to the database:")
    print("1: add new words one by one")
    print("2: add new words from a file")
    print("\nPlay games:")
    print("3: play to 'Spaces'")
    print("\nOthers:")
    print("4: show all the words in the database")
    print("5: exit")

    response = input("\n")

    if response == "1":
        Dic = DataBase.add_single(Dic)
    elif response == "2":
        Dic = DataBase.add_from_file(Dic)
    elif response == "3":
        Game1_Spaces.game(Dic)
    elif response == "4":
        DataBase.show(Dic)
    else:
        print("\nOk, see you soon!\n")
        DataBase.close_DB(Dic)
        break


