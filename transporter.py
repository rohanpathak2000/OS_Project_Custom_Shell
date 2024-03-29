from cmd import Cmd

import os
from prettytable import PrettyTable

def login():
    global currUser
    global session
    flag = 0
    user_file = open("./transporter/transporters.txt", "r")
    user_snippet_list = user_file.readlines()
    uname = input(" Username : ")
    pwd = input(" Password : ")
    for user_snippet in user_snippet_list:
        user = user_snippet.split('  ')
        if user[0] == uname:
            #print(user[0])
            if user[2] == pwd:
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
    users_file = open("./transporter/transporters.txt","r")
    user_snippet_list = users_file.readlines()
    uname = input(" Enter username : ")
    fname = input(" Enter first name : ")
    lname = input(" Enter last name : ")
    pwd = input(" Enter password : ")
    new_user = uname + "  " + fname + " " + lname + "  " + pwd + "  " + "\n"
    if len(user_snippet_list) > 0:
        for user_snippet in user_snippet_list:
          user = user_snippet.split('  ')
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
            with open("./transporter/transporters.txt","a") as users_file:
                users_file.write(new_user)
                currUser = uname
                return 1
    else:
        with open("./transporter/transporters.txt","a") as users_file:
            users_file.write(new_user)
            currUser = uname
            return 1

table = PrettyTable(['Item id','Name','Qty','Rate','Shopkeeper Id'])

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
            if session==1:
                row=[-1,-1,-1,-1,-1]
                items_file = open("./transporter/transp.txt","r")
                item_snippet_list = items_file.readlines()
                for item_snippet in item_snippet_list:
                    item = item_snippet.split(' ')
                    if(item[-3]==currUser):
                        for i in range(0,4):
                            row[i]=item[i]
                        row[-1]=item[-2]
                        table.add_row(row)
                print(table)

    def do_dvcnf(self, inp):
        if session == 1:
            cmnd = "python ./transporter/delivery_confirmed.py " + currUser
            os.system(cmnd)
        else:
            print("Register or Login first !!!!\nRefer help for commands to login or register")

    def do_retnpc(self, inp):
        if session == 1:
            cmnd = "python ./transporter/return_pickup.py " + currUser
            os.system(cmnd)
        else:
            print("Register or Login first !!!!\nRefer help for commands to login or register")     

    def do_help(self, inp):
        print("\nList of commands\n----------------")
        print("1.login - To login if you already have an account\n2.register - If you are new and wish to create a new account")
        print("3.dvcnf - To Too confirm a delivery\n4.viewitem - To view the items that have been assigned to you")
        print("5.retnpc - To pickup the returned goods")

    def do_logout(self, inp):
        global session
        session = 0

MyPrompt().cmdloop()
print("How was the experience?")
