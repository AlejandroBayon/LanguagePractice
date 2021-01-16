import json

def open_DB():
    with open("DataBase.txt") as file:
        Dic = json.load(file)
    return Dic


def close_DB(Dic):
    with open("DataBase.txt", "w") as file:
        json.dump(Dic, file)
    
def add(Dic):
    adding = 1
    while adding == 1:
        key = input("\nEnter a new word: ")
        value = input("Enter its definition: ")
        Dic[key] = value
        option = input("\nDo you want to add more words? ")
        if option == "No" or option == "no":
            adding = 0
    else:
        return Dic