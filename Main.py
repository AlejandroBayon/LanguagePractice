#Main script from where the games are called

import DataBase

Dic = DataBase.open_DB()

print("What do you want to do?")
print("1: add new words to the dictionary")

response = input()

if response == "1":
    Dic = DataBase.add(Dic)
else:
    print("Ok, goodbye!")

DataBase.close_DB(Dic)


