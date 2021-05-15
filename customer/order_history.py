import sys
from pathlib import Path

data_folder = Path("E:\Win2020-21\OS\Project")
currUser = sys.argv[1]

def findTrans(od):
    file_to_open = data_folder / "transporter/transporters.txt"
    trans_file = open(file_to_open,"r")
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
    file_to_open = data_folder / "shopkeeper/shops.txt"
    shops_file = open(file_to_open,"r")
    shop_snippet_list = shops_file.readlines()
    for shop_snippet in shop_snippet_list:
        shop = shop_snippet.split(' ')
        if shop[0] == od:
            sp = " ".join(shop[1:])
            return sp    
    shops_file.close()

file_to_open = data_folder / "customer/orders.txt"
orders_file = open(file_to_open, "r")
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

ptr = 1
while ptr:
    ch = input("Do you wish to delete any order from history ? [Y/N] ")
    flag = 1
    if ch == 'Y':
        order_id = input("Enter the order id : ")
        itm_name = input("Enter the item name : ")
        orders_file = open(file_to_open, "r")
        order_snippet_list = orders_file.readlines()
        with open(file_to_open, "w") as orders_file:
            for order_snippet in order_snippet_list:
                order = order_snippet.split(' ')
                if order[0] == order_id and order[1] == itm_name:
                    if order[4] == "delivered":
                        continue
                    else:
                        flag=0
                orders_file.write(order_snippet)
            if flag == 0:
                print("The order could not be deleted from history as it is not delivered yet ")
            else:
                print("Order deleted from the history successfully !!!")
    elif ch == 'N':
        ptr = 0