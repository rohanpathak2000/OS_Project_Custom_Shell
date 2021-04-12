def findShop(od):
    shops_file = open("shops.txt","r")
    shop_snippet_list = shops_file.readlines()
    for shop_snippet in shop_snippet_list:
        shop = shop_snippet.split(' ')
        if shop[0] == od:
            sp = " ".join(shop[1:])
            return sp    
    shops_file.close()

def findTrans(od):
    trans_file = open("transporters.txt","r")
    trans_snippet_list = trans_file.readlines()
    for trans_snippet in trans_snippet_list:
        trans = trans_snippet.split(' ')
        if trans[0] == od:
            trans = trans[1:]
            last_name = trans[-1]
            last_name = last_name[:-1]
            trans[-1] = last_name
            tr = " ".join(trans)
            return tr
    trans_file.close()        
    
def register():
    flag = 1
    global currUser
    users_file = open("users.txt","r")
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
            with open("users.txt","a") as users_file:
                users_file.write(new_user)
                currUser = uname
                return 1
    else:
        with open("users.txt","a") as users_file:
            users_file.write(new_user)
            currUser = uname
            return 1
            
currUser = " None "

def login():
    global currUser
    flag = 0
    user_file = open("users.txt", "r")
    user_snippet_list = user_file.readlines()
    uname = input(" Username : ")
    pwd = input(" Password : ")
    for user_snippet in user_snippet_list:
        user = user_snippet.split(' ')
        if user[0] == uname:
            #print(user[0])
            if user[3] == pwd+"\n":
                #print(user[3])
                currUser = uname
                flag = 1
                break
    user_file.close()
    return flag
    

print(" In order to you must be signed in. How do you wish to proceed ")
print(" 1. Already have an account ? Sign in " )
print(" 2. New User ? Register ")
choice = int(input(" Enter Choice :  "))
if choice == 1:
    session = login()
else:
    session = register()

print(currUser)

if session == 1:
    orders_file = open("orders.txt", "r")
    order_snippet_list = orders_file.readlines()
    for order_snippet in order_snippet_list:
        order = order_snippet.split(' ')
        if order[-1] == currUser + "\n" and order[4] != "in_cart":
            for od in order:
                if od != currUser + "\n":
                    if "sp" in od:
                        shop_name = findShop(od)
                        print(shop_name,end="")                
                    elif "tp" in od:
                        trans_name = findTrans(od)
                        print(trans_name + " ",end="")
                    else:
                        print(od + " ",end="")
        if order[-1] == currUser + "\n":
            print("")

ch = input("Do you wish to delete any order from history ? [Y/N] ")

flag = 1

if ch == 'Y':
    order_id = input("Enter the order id : ")
    orders_file = open("orders.txt", "r")
    order_snippet_list = orders_file.readlines()
    with open("orders.txt", "w") as orders_file:
        for order_snippet in order_snippet_list:
            order = order_snippet.split(' ')
            if order[0] == order_id:
                if order[4] == "delivered":
                    continue
                else:
                    flag=0
            orders_file.write(order_snippet)
        if flag == 0:
            print("The order could not be completed as it is not delivered yet ")
        else:
            print("Order deleted from the history successfully !!!")
        