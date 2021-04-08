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
    #print(order)
    order.append(currUser+"\n")
    order = " ".join(order)
    #print(order)
    with open("orders.txt","a") as orders_file:
        orders_file.write(order)


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
            print(user[0])
            if user[3] == pwd+"\n":
                print(user[3])
                currUser = uname
                flag = 1
                break
    user_file.close()
    return flag

currUser = " None "


            
def confirm_order():
    ptr = 0
    orders_file = open("orders.txt","r")
    order_snippet_list = orders_file.readlines()
    if len(order_snippet_list)>0:
            with open("orders.txt","w") as orders_file: 
                for order_snippet in order_snippet_list:
                    order = order_snippet.split(' ')
                    if order[4] == "in_cart" and order[-1] == currUser+"\n":
                        ptr = 1
                        order[4] = "pending"
                        updated_order_snippet = " ".join(order)
                        orders_file.write(updated_order_snippet)
                        continue
                    orders_file.write(order_snippet)
            if ptr == 0:
                print(" Nothing in cart ")
            else:
                print("Order Placed Successfully !!")
    else:                    
        print("Nothing in cart ...")           
         
     
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


cart = []               
order_id = 1
ongoing_order = True
order_success = False
items_file = open("items.txt","r")
orders_file = open("orders.txt","r")
order_snippet_list = orders_file.readlines()
if len(order_snippet_list)>0:
    last_order = order_snippet_list[-1]
    print(last_order[3])
    if int(last_order[3]) > 0:
        order_id = int(last_order[3]) + 1 

            
orders_file.close()

print(" In order to you must be signed in. How do you wish to proceed ")
print(" 1. Already have an account ? Sign in " )
print(" 2. New User ? Register ")
choice = int(input(" Enter Choice :  "))
if choice == 1:
    session = login()
else:
    session = register()

print(currUser)
flag = 1
if session == 1:
    while flag==1:
        print("1. View Cart ")
        print("2. Add to Cart ")
        print("3. Delete from Cart ")
        print("4. Place the order ")
        print("5. Exit ")
        ch = input("Enter choice : ")
        if ch == '2':
            while ongoing_order:
                with open("items.txt", "r") as items_file:
                    item_detail_snippets_list = items_file.readlines()  
                with open("items.txt", "w") as items_file:
                    item_found = False
                    order_success = False
                    item_id = input("Enter Id of Item : ")
                    item_qty = int(input("Enter the qty of purchase : "))
                    for item_detail_snippet in item_detail_snippets_list:
                        #print(item_detail_snippet)
                        item = item_detail_snippet.split(' ')
                        #pint(item)
                        #print(item[1])
                        if item[0] == item_id:
                            item_found = True
                            if int(item[3]) >= item_qty:
                                issue_order(item, item_qty, order_id)
                                item[3] = int(item[3]) - item_qty
                                item[3] = str(item[3])
                                order_success = True
                                updated_item_detail_snippet = " ".join(item)
                                items_file.write(updated_item_detail_snippet)
                                continue      
                        items_file.write(item_detail_snippet)    
                if order_success:
                    print("Item Added !!")
                else:
                    if item_found == False:
                        print("Item Not Found !!")
                    else:
                        print("Stock Unavailable !!")
                ch = input("Would you like to order more items [Y/N] : ")
                if ch=='N':
                    ongoing_order = False
        elif ch == '1':
            print(" ----- Cart Items ----")
            orders_file = open("orders.txt","r")
            order_snippet_list = orders_file.readlines()
            if len(order_snippet_list)>0:
                for order_snippet in order_snippet_list:
                    order = order_snippet.split(' ')
                    if order[4] == "in_cart" and order[6] == currUser+"\n":
                        for od in order:
                            if od != "in_cart" and od != currUser+"\n":
                                print(od + " ",end="")
                        print("\n")    
            print(" ")
        elif ch == '3':
            ptr = 0
            ord_id = input("Enter order id: ")
            item_name = input("Enter item name : ")
            orders_file = open("orders.txt","r")
            order_snippet_list = orders_file.readlines()
            with open("orders.txt","w") as orders_file:
                for order_snippet in order_snippet_list:
                    order = order_snippet.split(' ')
                    if order[1] == item_name and order[0] == ord_id:
                        ptr = 1
                        continue
                    orders_file.write(order_snippet)
            if ptr == 0:
                print("Item not found ...")
        elif ch == '4':
            print(" ----- Cart Items ----")
            orders_file = open("orders.txt","r")
            order_snippet_list = orders_file.readlines()
            if len(order_snippet_list)>0:
                for order_snippet in order_snippet_list:
                    order = order_snippet.split(' ')
                    if order[4] == "in_cart" and order[6] == currUser+"\n":
                        for od in order:
                            if od != "in_cart" and od != currUser+"\n":
                                print(od + " ",end="")
                        print("\n")    
            print(" ")
            ch = input("Are you sure you want to put the order ? [Y/N] ")
            if ch == 'Y':
                confirm_order()
        elif ch == '5':
            flag=0
else:
    print("Username or Password not found ")
