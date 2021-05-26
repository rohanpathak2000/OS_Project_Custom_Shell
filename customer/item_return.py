import sys
from pathlib import Path
from prettytable import PrettyTable

currUser = sys.argv[1]
data_folder = Path("E:\Win2020-21\OS\Project")

table = PrettyTable(['Order id', 'Name', 'Qty', 'Cost', 'Transporter', 'Shop'])


def findTrans(od):
    file_to_open = data_folder / "transporter/transporters.txt"
    trans_file = open(file_to_open,"r")
    trans_snippet_list = trans_file.readlines()
    for trans_snippet in trans_snippet_list:
        trans = trans_snippet.split('  ')
        if trans[0] == od:
            tr = trans[1]
            return tr
    trans_file.close()

def findShop(od):
    file_to_open = data_folder / "shopkeeper/shopkeeper.txt"
    shops_file = open(file_to_open,"r")
    shop_snippet_list = shops_file.readlines()
    for shop_snippet in shop_snippet_list:
        shop = shop_snippet.split(' ')
        if shop[0] == od:
            sp = " ".join(shop[1:])
            return sp    
    shops_file.close()

ptr = 0
found = False
file_to_open = data_folder / "customer/orders.txt"
orders_file = open(file_to_open,"r")
order_snippet_list = orders_file.readlines()
for order_snippet in order_snippet_list:
    order = order_snippet.split(' ')
    row = []
    if order[4] == "delivered" and order[-1] == currUser + "\n":
        found = True
        for od in order:
            if od != currUser + "\n" and od != "delivered":
                if "sp" in od:
                    shop_name = findShop(od)
                    row.append(shop_name)
                    #print(shop_name,end="")                
                elif "tp" in od:
                    trans_name = findTrans(od)
                    row.append(trans_name)
                    #print(trans_name + " ",end="")
                else:
                    row.append(od)
                    #print(od + " ",end="")
        table.add_row(row)
print()
if found:
    print(table)
else:
    print("!!!! No items which can be returned !!!!")

if found: 
    ord_id = input("Enter the order id : ")
    item_name = input("Enter the name of the item : ")
    with open(file_to_open,"w") as orders_file:
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
            print("Invalid Operation !!! ")

table.clear_rows()