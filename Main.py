#Main script from where the games are called

import DataBase
import Game1_Spaces

Dic = DataBase.open_DB()
executing = 1

while executing == 1:
    print("What do you want to do?")
    print("1: add new words to the dictionary")
    print("2: play to 'Spaces'")
    print("3: exit")

    response = input()

    if response == "1":
        Dic = DataBase.add(Dic)
    elif response == "2":
        Game1_Spaces.game(Dic)
    else:
        print("Ok, goodbye!")
        DataBase.close_DB(Dic)
        break


