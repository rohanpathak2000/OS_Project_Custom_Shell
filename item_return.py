import sys

currUser = sys.argv[1]




def findTrans(od):
    trans_file = open("../transporter/transporters.txt","r")
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

def findShop(od):
    shops_file = open("../shopkeeper/shops.txt","r")
    shop_snippet_list = shops_file.readlines()
    for shop_snippet in shop_snippet_list:
        shop = shop_snippet.split(' ')
        if shop[0] == od:
            sp = " ".join(shop[1:])
            return sp    
    shops_file.close()

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