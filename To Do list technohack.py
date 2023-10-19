# from helper import welcome_msg
import os
from datetime import date

def welcome_msg(name):
    print(f""" **WELCOME $ {name} $ TO TO_DO_LISTS APPLICATION**
        1--> UPDATE LIST
        2--> TRACK LIST
        3--> exit""")

def to_do_create(name):
    """ This Function takes 'name' as a parameter just Creates a text file having name of the User and Displays a message that List_file is Created"""
    with open(f"{name}.txt", 'a')as f:
        f.write("")
    print("To do List_File is created Successfully")


def update(name):
    """ Update Function takes 'User_Name' as a parameter and Provide User to Add or Remove Tasks as Well as to delelte their list."""
    print(f"Welcome, {name} to EDIT Menu")
    choice = int(
        input("Press '1' to ADD '2' to REMOVE tasks and '3' to DELETE List_File: "))
    if choice == 1:
        task = input("Enter Task to ADD: ")
        with open(f"{name}.txt", 'a') as f:
            f.write(f"{task} - {date.today()}\n")
    elif choice == 2:
        task = input("Enter Task to DELETE: ")
        try:
            # ISSUE HERE
            new_list = ""
            with open("name.txt", 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if task not in line:
                        new_list += line + "\n"
            with open(f"{name}.txt", 'w') as f:
                f.write(new_list)
        except:
            print("OOPs, Something gone Wrong!! CAN'T REMOVE THIS TASK")

    elif choice == 3:
        try:
            os.remove(f"{name}.txt")
            print(f"{name} list_file Deleted Successfully")
        except:
            print("Something gone Wrong!!")
    else:
        print("Invalid Choice")


def track(name):
    """This function just Outputs the text file that has given by the Parameter;"""
    try:
        with open(f"{name}.txt", 'r')as f:
            result = f.read()
            if (result == ""):
                print("No Task Here")
            else:
                print(result)
    except FileNotFoundError:
        print(
            f"List with the UserName '{name}' NOT FOUND, please first ADD your List")


name = input("Please Enter Your Name: ")
to_do_create(name)
while (True):
    welcome_msg(name)
    choice = int(input("Enter Choice: "))
    if choice == 1:
        update(name)
    elif choice == 2:
        track(name)
    elif choice == 3:
        exit
    else:
        print("Invalid Choice")
