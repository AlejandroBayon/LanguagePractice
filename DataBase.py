import json
import re
import os
import time

def open_DB():
    with open("DataBase.txt") as file:
        Dic = json.load(file)
    return Dic


def close_DB(Dic):
    with open("DataBase.txt", "w") as file:
        json.dump(Dic, file)
    
def add_single(Dic):
    os.system("cls")
    adding = 1
    while adding == 1:
        key = input("Enter a new word: ")
        value = input("Enter its definition: ")
        Dic[key] = value
        option = input("\nDo you want to add more words? ")
        if option == "No" or option == "no":
            adding = 0
        else:
            print()
    return Dic

def add_from_file(Dic):
    os.system("cls")
    input_file = input("From which file do you want to add new words? ")
    if os.path.exists(input_file):
        try:
            with open(input_file) as file:
                for row in file:
                    new_row = row.strip()
                    key, value = re.split(": ", new_row)
                    Dic[key] = value
            print("\nNew words added successfully!\n")
        except:
            print("\nAn error occurred, the words can't be added\n")
    else:
        print("\nSorry, this file doesn't exist\n")
    time.sleep(4)
    return Dic

def show(Dic):
    os.system("cls")
    print("There are " + str(len(Dic)) + " words in the database\n")
    for word, definition in sorted(Dic.items()):
        print(word + ": " + definition)
    input("\n")

def clear(Dic):
    os.system("cls")
    response = input("Are you sure you want to empty the database? ")
    if response == "Yes" or response == "yes":
        Dic.clear()
        print("\nDatabase emptied successfully\n")
    time.sleep(4)
    return Dic