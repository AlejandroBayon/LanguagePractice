import json
import re
import os

def open_DB():
    with open("DataBase.txt") as file:
        Dic = json.load(file)
    return Dic


def close_DB(Dic):
    with open("DataBase.txt", "w") as file:
        json.dump(Dic, file)
    
def add_single(Dic):
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

def add_from_file(Dic):
    input_file = input("\nFrom which file do you want to add new words? ")
    if os.path.exists(input_file):
        try:
            with open(input_file) as file:
                for row in file:
                    new_row = row.strip()
                    key, value = re.split(": ", new_row)
                    Dic[key] = value
            print("\nNew words added successfully!")
        except:
            print("\nAn error occurred, the words can't be added")
    else:
        print("\nSorry, this file doesn't exist")
    return Dic

def show(Dic):
    print("\nThere are " + str(len(Dic)) + " words in the database\n")
    for word, definition in sorted(Dic.items()):
        print(word + ": " + definition)

def clear(Dic):
    response = input("\nAre you sure you want to empty the database? ")
    if response == "Yes" or response == "yes":
        Dic.clear()
        print("\nDatabase emptied successfully")
    return Dic