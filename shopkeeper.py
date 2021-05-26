from cmd import Cmd

import os
from prettytable import PrettyTable

def login():
    global currUser
    global session
    flag = 0
    user_file = open("./shopkeeper/shopkeeper.txt", "r")
    user_snippet_list = user_file.readlines()
    uname = input(" Username : ")
    pwd = input(" Password : ")
    for user_snippet in user_snippet_list:
        user = user_snippet.split(' ')
        if user[0] == uname:
            #print(user[0])
            if user[3] == pwd:
                currUser=uname
                print("Redirecting...")
                flag = 1
                break
    user_file.close()
    return flag

def register():
    flag = 1
    global currUser
    global session
    users_file = open("./shopkeeper/shopkeeper.txt","r")
    user_snippet_list = users_file.readlines()
    uname = input(" Enter username : ")
    fname = input(" Enter first name : ")
    lname = input(" Enter last name : ")
    pwd = input(" Enter password : ")
    new_user = uname + " " + fname + " " + lname + " " + pwd + "\n"
    if len(user_snippet_list) > 0:
        for user_snippet in user_snippet_list:
          user = user_snippet.split(' ')
          if user[0] == uname:
            flag = 0
            break
        if flag == 0:
            print("Username already taken ")
            ch = input("Do you wish to try again ? [Y/N] ")
            if ch == 'Y':
                return register()
            else:
                return 0
        else:
            with open("./shopkeeper/shopkeeper.txt","a") as users_file:
                users_file.write(new_user)
                currUser = uname
                return 1
    else:
        with open("./shopkeeper/shopkeeper.txt","a") as users_file:
            users_file.write(new_user)
            currUser = uname
            return 1

table = PrettyTable(['Item id','Name','Category','Rate','Available Qty'])

class MyPrompt(Cmd):
    def do_exit(self, inp):
        print(" Exiting .....")
        return True

    def do_login(self, inp):
        global session
        session = login()
        if session == 0:
            print("Username or Password is incorrect")
  
    def do_register(self, inp):
        global session
        session = register()

    def do_viewitem(self, inp):
            print("Lookup by \n1. Category Name\n2. Item name")
            if currUser == 'sp_1' and session==1:
                items_file = open("items.txt","r")
                item_snippet_list = items_file.readlines()
                for item_snippet in item_snippet_list:
                    item = item_snippet.split(' ')
                    if item[2]=="fruits":
                        table.add_row(item)
                print(table)

            elif currUser == 'sp_2' and session==1:
                items_file = open("items.txt","r")
                item_snippet_list = items_file.readlines()
                for item_snippet in item_snippet_list:
                    item = item_snippet.split(' ')
                    if item[2]=="dairy":
                        table.add_row(item)
                print(table)

    def do_additem(self, inp):
        if session == 1:
            cmnd = "python ./shopkeeper/add_item.py "
            os.system(cmnd)
        else:
            print("Register or Login first !!!!\nRefer help for commands to login or register")

    def do_itemdispatch(self, inp):
        if session == 1:
            cmnd = "python ./shopkeeper/item_dispatch.py "
            os.system(cmnd)
        else:
            print("Register or Login first !!!!\nRefer help for commands to login or register")

    def do_ordercancel(self, inp):
        if session == 1:
            cmnd = "python ./shopkeeper/order_cancelled.py "
            os.system(cmnd)
        else:
            print("Register or Login first !!!!\nRefer help for commands to login or register")       

    def do_help(self, inp):
        print("\nList of commands\n----------------")
        print("1.login - To login if you already have an account\n2.register - If you are new and wish to create a new account")
        print("3.additem - To add a particular item in your shop\n4.viewitem - To view the items in your cart")
        print("4.itemdispatch - To dispatch the items ordered by the customer")
        print("5.ordercancel - To cancel the dispatch any particular item")
        print("6.orderHistory - View your order history\n")

    def do_logout(self, inp):
        global session
        session = 0

MyPrompt().cmdloop()
print("well done")