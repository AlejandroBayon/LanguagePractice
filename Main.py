#Main script from where the games are called

import DataBase
import Game1_Spaces

Dic = DataBase.open_DB()
executing = 1
print("\nWelcome to LANGUAGE PRACTICE!\n")

while executing == 1:
    print("What do you want to do?\n")
    print("Add new words to the database:")
    print("1: add new words one by one")
    print("2: add new words from a file")
    print("\nPlay games:")
    print("3: play to 'Spaces'")
    print("\n4: exit")

    response = input("\n")

    if response == "1":
        Dic = DataBase.add_single(Dic)
    elif response == "2":
        Dic = DataBase.add_from_file(Dic)
    elif response == "3":
        Game1_Spaces.game(Dic)
    else:
        print("\nOk, see you soon!\n")
        DataBase.close_DB(Dic)
        break


