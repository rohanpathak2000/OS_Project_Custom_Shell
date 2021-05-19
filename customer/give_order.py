import sys
from pathlib import Path
from prettytable import PrettyTable
data_folder = Path("E:\Win2020-21\OS\Project")
currUser = sys.argv[1]


def confirm_order():
    ptr = 0
    file_to_open = data_folder / "customer/orders.txt"
    orders_file = open(file_to_open,"r")
    order_snippet_list = orders_file.readlines()
    if len(order_snippet_list)>0:
            with open(file_to_open,"w") as orders_file: 
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

table = PrettyTable(['Order id','Item','Qty','Cost','Transporter','Shopkeeper'])

print(" ----- Cart Items ----- ")
file_to_open = data_folder / "customer/orders.txt"
orders_file = open(file_to_open,"r")
order_snippet_list = orders_file.readlines()
if len(order_snippet_list)>0:
    for order_snippet in order_snippet_list:
        row = []
        transp_found = False
        order = order_snippet.split(' ')
        if order[4] == "in_cart" and order[6] == currUser+"\n":
            for od in order:
                if od != "in_cart" and od != currUser+"\n":
                    if "sp" in od:
                        shop_name = findShop(od)
                        row.append(shop_name)
                        #print(shop_name,end="\t\t")
                    elif "tp" in od:
                        trans_name = findTrans(od)
                        transp_found = True
                        row.append(trans_name)
                        #print(trans_name,end="\t\t")
                    else:
                        row.append(od)
                        #print(od,end="\t\t")            
            if transp_found == False:
                shp = row[-1]
                row[-1] = 'NA'
                row.append(shp)
            table.add_row(row)
    print(table)
            #print()
            
   
                
print("")
ch = input("Are you sure you want to put the order ? [Y/N] ")
if ch == 'Y':
   confirm_order()