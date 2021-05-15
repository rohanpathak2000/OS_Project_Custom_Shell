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



print(" ----- Cart Items ----")
file_to_open = data_folder / "customer/orders.txt"
orders_file = open(file_to_open,"r")
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
            
            