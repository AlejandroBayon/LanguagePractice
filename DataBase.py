import json

def open_DB():
    with open("DataBase.txt") as file:
        Dic = json.load(file)
    print("Database opened")
    return Dic


def close_DB(Dic):
    with open("DataBase.txt", "w") as file:
        json.dump(Dic, file)
    print("Database closed")

def add(Dic):
    adding = 1
    while adding == 1:
        key = input("Word: ")
        value = input("Definition: ")
        Dic[key] = value
        option = input("Do you want to add more words? Yes or No: ")
        if option == "No":
            adding = 0
    else:
        return Dic