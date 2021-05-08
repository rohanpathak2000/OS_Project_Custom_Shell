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
            if user[3] == pwd:
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
        
        
def findShop(od):
    shops_file = open("shops.txt","r")
    shop_snippet_list = shops_file.readlines()
    for shop_snippet in shop_snippet_list:
        shop = shop_snippet.split(' ')
        if shop[0] == od:
            sp = " ".join(shop[1:])
            return sp    
    shops_file.close()


def updateInItems(item_to_update, qty_to_add):
    items_file = open("items.txt", "r")
    item_snippet_list = items_file.readlines()
    with open("items.txt","w") as items_file:
        for item_snippet in item_snippet_list:
            item = item_snippet.split(' ')
            if item[1] == item_to_update:
                item[3] = str(int(item[3]) + int(qty_to_add))
                updated_item = " ".join(item)    
                items_file.write(updated_item)
                continue
            items_file.write(item_snippet)
    items_file.close()        


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

              
order_id = 1
ongoing_order = True
order_success = False
items_file = open("items.txt","r")
orders_file = open("orders.txt","r")
order_snippet_list = orders_file.readlines()
if len(order_snippet_list)>0:
    last_order = order_snippet_list[-1]
    #print(last_order[3])
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

#print(currUser)

flag = 1
if session == 1:
    while flag==1:
        print("1. View Cart\n2. Add to Cart\n3. Delete from Cart\n4. Place the order\n6. View Profile\n7. Change Details\n8. View Order History\n9. Return an item\n5. Exit\n10. View All Items\n11. Search an item");
        ch = input("Enter choice : ")
        if ch == '2':
            while ongoing_order:
                with open("items.txt", "r") as items_file:
                    item_detail_snippets_list = items_file.readlines()  
                with open("items.txt", "w") as items_file:
                    item_found = False
                    order_success = False
                    item_id = input("Enter Id of Item : ")
                    for item_detail_snippet in item_detail_snippets_list:
                        item = item_detail_snippet.split(' ')
                        if item[0] == item_id:
                            item_found = True
                            item_qty = int(input("Enter the qty of purchase : "))
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
                                if "sp" in od:
                                    shop_name = findShop(od)
                                    print(shop_name + " ",end="")
                                elif "tp" in od:
                                    trans_name = findTrans(od)
                                    print(trans_name + " ",end="")
                                else:                                
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
                        qty_to_add = order[2]
                        item_to_update = order[1]
                        updateInItems(item_to_update, qty_to_add)
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
                                if "sp" in od:
                                    shop_name = findShop(od)
                                    print(shop_name + " ",end="")
                                elif "tp" in od:
                                    trans_name = findTrans(od)
                                    print(trans_name + " ",end="")
                                else:
                                    print(od + " ",end="")
                                    
                        print("")    
            print(" ")
            ch = input("Are you sure you want to put the order ? [Y/N] ")
            if ch == 'Y':
                confirm_order()
        elif ch == '5':
            flag=0
        elif ch == '7':
            print("1. Change Password ")
            print("2. Change Address ")
            c = input("Enter Choice : ")
            users_file = open("users.txt","r")
            user_snippet_list = users_file.readlines()
            if c == '1': 
                with open("users.txt","w") as users_file:
                    for user_snippet in user_snippet_list:
                        user = user_snippet.split(' ')
                        if user[0] == currUser:
                            new_pwd = input("Enter new password : ")
                            user[3] = new_pwd
                            updated_user = " ".join(user)
                            users_file.write(updated_user)
                            print("Password Updated successfully !! ")
                            continue
                        users_file.write(user_snippet)
            elif c=='2':
                with open("users.txt","w") as users_file:
                    for user_snippet in user_snippet_list:
                        user = user_snippet.split(' ')
                        if user[0] == currUser:
                            new_addr = input("Enter the new address : ")
                            new_addr = new_addr + "\n"
                            user[4] = new_addr
                            updated_user = " ".join(user)
                            users_file.write(updated_user)
                            continue
                        users_file.write(user_snippet)
                        
        
        elif ch == '6':
            users_file = open("users.txt","r")
            user_snippet_list = users_file.readlines()
            for user_snippet in user_snippet_list:
                user = user_snippet.split(' ')
                if user[0] == currUser:
                    print("Username : " + currUser + "\nName : " + user[1] + " " + user[2] + "\nAddress : " + " ".join(user[4:]))
        elif ch == '8':
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
        elif ch == '9':
            ptr = 0
            orders_file = open("orders.txt","r")
            order_snippet_list = orders_file.readlines()
            for order_snippet in order_snippet_list:
                order = order_snippet.split(' ')
                if order[4] == "delivered" and order[-1] == currUser + "\n":
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
            ord_id = input("Enter the order id : ")
            item_name = input("Enter the name of the item : ")
            with open("orders.txt","w") as orders_file:
                for order_snippet in order_snippet_list:
                    order = order_snippet.split(' ')
                    if order[0] == ord_id and order[1] == item_name and order[-1] == currUser + "\n":
                        ptr = 1
                        order[4] = "return_p"
                        updated_order = " ".join(order)
                        orders_file.write(updated_order)
                        continue
                    orders_file.write(order_snippet)
                if ptr == 1:
                    print("Request for return sent !!!")
                else:
                    print("Invalid Operation !! ")
        elif ch == '10':
            items_file = open("items.txt","r")
            item_snippet_list = items_file.readlines()
            for item_snippet in item_snippet_list:
                print(item_snippet,end='')
        elif ch == '11':
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
                
            
else:
    print("Username or Password not found ")
