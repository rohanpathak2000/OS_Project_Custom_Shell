from cmd import Cmd
import os

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
            print(user[0])
            if user[3] == pwd:
                print(user[3])
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

class MyPrompt(Cmd):
    def do_exit(self, inp):
        print("Bye")
        return True
        
    def do_login(self, inp):
        global session
        session = login()
            
    def do_register(self, inp):
        global session
        session = register()
        
    def do_items(self, inp):
            items_file = open("items.txt","r")
            item_snippet_list = items_file.readlines()
            for item_snippet in item_snippet_list:
                print(item_snippet,end='')
    
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
                        print(item_snippet)
            elif c == '2':
                items_file = open("items.txt","r")
                itm_name = input("Enter name : ")
                for item_snippet in item_snippet_list:
                    item = item_snippet.split(' ')
                    if item[1] == itm_name:
                        print(item_snippet)
                        
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
        
        
        
    def do_shopkeeper(self, inp):
        print("enter your shop id")
        shop_id=input()

        if(shop_id=="sp_1"):
                with open('orders.txt', 'r') as items_file:
                        items = items_file.readlines()
                        for item in items:
                                print(item)
                print("				")
                print("Enter the Id of Order to be dispatched ")
                item_id = input()
                with open('orders.txt', 'w') as mater_file:
                        for item in items:
                                item_content = item.split(" ")
                                if str(item_content[0]) == item_id  and item_content[5]=="sp_1":
                                        with open('transp.txt','a') as tp_file:
                                                item_content[4]="arriving tp_7"
                                                join=" ".join(item_content)
                                                tp_file.write(join)
                                                mater_file.write(join)
                                        continue
                                mater_file.write(item)

        elif(shop_id=="sp_2"):
                with open('orders.txt', 'r') as items_file:
                        items = items_file.readlines()
                        for item in items:
                                print(item)
                print("				")
                print("Enter the Id of Order to be dispatched ")
                item_id = input()
                with open('orders.txt', 'w') as mater_file:
                        for item in items:
                                item_content = item.split(" ")
                                if str(item_content[0]) == item_id  and item_content[5]=="sp_2":                                
                                        with open('transp2.txt','a') as tp_file:
                                                item_content[4]="arriving tp_8"
                                                join=" ".join(item_content)
                                                tp_file.write(join)
                                                mater_file.write(join)
                                        continue
                                mater_file.write(item)

    
MyPrompt().cmdloop()
print("After")