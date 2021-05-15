import sys
from pathlib import Path

data_folder = Path("E:\Win2020-21\OS\Project")

currUser = sys.argv[1]

def issue_order(item, qty, order_id):
    file_to_open = data_folder / "customer/orders.txt" 
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
    with open(file_to_open,"a") as orders_file:
        orders_file.write(order)

file_to_open = data_folder / "items.txt" 

order_id = 1
ongoing_order = True
order_success = False
items_file = open(file_to_open,"r")

file_to_open = data_folder / "customer/orders.txt"
 
orders_file = open(file_to_open,"r")
order_snippet_list = orders_file.readlines()
if len(order_snippet_list)>0:
    last_order = order_snippet_list[-1]
    #print(last_order[3])
    last_order_detail = last_order.split(' ')
    last_order_id = last_order_detail[0]
    orderId = last_order_id[3:]
    if int(orderId) > 0:
        order_id = int(orderId) + 1 

while ongoing_order:
    file_to_open = data_folder / "items.txt" 
    with open(file_to_open, "r") as items_file:
        item_detail_snippets_list = items_file.readlines()  
    with open(file_to_open, "w") as items_file:
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