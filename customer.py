from cmd import Cmd
import os
from prettytable import PrettyTable

def login():
    global currUser
    global session
    flag = 0
    user_file = open("./customer/users.txt", "r")
    user_snippet_list = user_file.readlines()
    uname = input(" Username : ")
    pwd = input(" Password : ")
    for user_snippet in user_snippet_list:
        user = user_snippet.split(' ')
        if user[0] == uname:
            #print(user[0])
            if user[3] == pwd:
                #print(user[3])
                currUser = uname
                flag = 1
                break
    user_file.close()
    return flag

def register():
    flag = 1
    global currUser
    global session
    users_file = open("./customer/users.txt","r")
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
            with open("./customer/users.txt","a") as users_file:
                users_file.write(new_user)
                currUser = uname
                return 1
    else:
        with open("./customer/users.txt","a") as users_file:
            users_file.write(new_user)
            currUser = uname
            return 1
            
def issue_order(item, qty, order_id):
    order = []
    order.append("od_" + str(order_id))
    order.append(item[1])
    order.append(str(qty))
    total_price = int(item[4]) * qty
    order.append(str(total_price))
    order.append("in_cart")
    if int(item[0])>=1 and int(item[0])<=5:
        order.append("sp_1")
    elif int(item[0])>=6 and int(item[0])<=10:
        order.append("sp_2")
    order.append(currUser+"\n")
    order = " ".join(order)
    with open("./customer/orders.txt","a") as orders_file:
        orders_file.write(order)


currUser = " "
session = 0

print("\n             ************* Welcome to our customer portal *************                \n")
print("         Type 'help' in order to look at the commands for navigating the portal easily           ")
print("\n-----------------------------------------------------------------------------------------------")

table = PrettyTable(['Item id','Name','Category','Rate','Available Qty'])

class MyPrompt(Cmd):
    def do_exit(self, inp):
        print(" !!!!!!!  Visit Us Again Soon !!!!!!!")
        return True
        
    def do_help(self, inp):
        print("\nList of commands\n----------------")
        print("1.login - To login if you already have an account\n2.register - If you are new and wish to create a new account")
        print("3.items - To view all the items available in the different shops\n4.lookup - To search for a particular item")
        print("4.addtocart - To add items in your cart\n6.delfromcart - To delete items from your cart")
        print("5.cart - View the items in your cart\n6.order - To place the order for the items in the cart\n7.profile - To view or update your profile")
        print("6.orderHistory - View your order history\n")
        
        
 
    def do_login(self, inp):
        global session
        session = login()
        if session == 0:
            print("Username or Password is incorrect")
  
    def do_register(self, inp):
        global session
        session = register()
        
    def do_items(self, inp):
            items_file = open("items.txt","r")
            item_snippet_list = items_file.readlines()
            for item_snippet in item_snippet_list:
                item = item_snippet.split(' ')
                item[-1] = item[-1][:-1]
                table.add_row(item)
            print(table)
                
    
    def do_lookup(self, inp):
            print("Lookup by \n1. Category Name\n2. Item name")
            c = input("Enter Choice : ")
            if c == '1':
                items_file = open("items.txt","r")
                cat_name = input("Enter name : ")
                item_snippet_list = items_file.readlines()
                for item_snippet in item_snippet_list:
                    item = item_snippet.split(' ')
                    if item[2] == cat_name:
                        item[-1] = item[-1][:-1]
                        table.add_row(item)
                print(table)    
                        
            elif c == '2':
                items_file = open("items.txt","r")
                itm_name = input("Enter name : ")
                item_snippet_list = items_file.readlines()
                for item_snippet in item_snippet_list:
                    item = item_snippet.split(' ')
                    if item[1] == itm_name:
                        item[-1] = item[-1][:-1]
                        table.add_row(item)
                print(table)
                        
                        
                        
    def do_addtocart(self, inp):
        if session == 1:
            cmnd = "python ./customer/add_to_cart.py " + currUser    
            os.system(cmnd)
        else:
            print("Register or Login first !!!!\nRefer help for commands to login or register")
    
    def do_cart(self, inp):
        if session == 1:
            cmnd = "python ./customer/view_cart.py " + currUser
            os.system(cmnd)
        else:
            print("Register or login first !!!!!\nRefer help for commands to login or register")
    
    def do_delfromcart(self, inp):
        if session == 1:
            cmnd = "python ./customer/del_from_cart.py " + currUser
            os.system(cmnd)
        else:
            print("Register or login first !!!!!\nRefer help for commands to login or register")
   
    def do_order(self, inp):
        if session == 1:
            cmnd = "python ./customer/give_order.py " + currUser
            os.system(cmnd)
        else:
            print("Register or login first !!!!!\nRefer help for commands to login or register")
       
    def do_profile(self, inp):
        if session == 1:
            cmnd = "python ./customer/profile.py " + currUser
            os.system(cmnd)
        else:
            print("Register or login first !!!!!\nRefer help for commands to login or register")
    
    def do_orderHistory(self, inp):
        if session == 1:
            cmnd = "python ./customer/order_history.py " + currUser
            os.system(cmnd)
        else:
           print("Register or login first !!!!!\nRefer help for commands to login or register") 
        
    def do_return(self, inp):
        if session == 1:
            cmnd = "python ./customer/item_return.py " + currUser
            os.system(cmnd)
        else:
            print("Register or login first !!!!!\nRefer help for commands to login or register") 
        
    def do_logout(self, inp):
        global session
        session = 0
        
MyPrompt().cmdloop()