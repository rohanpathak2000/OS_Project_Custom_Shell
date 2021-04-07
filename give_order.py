def issue_order(item, qty, order_id):
    order = []
    order.append("od_" + str(order_id))
    order.append(item[1])
    order.append(str(qty))
    total_price = int(item[4]) * qty
    order.append(str(total_price) +  "\n")
    #print(order)
    order = "    ".join(order)
    #print(order)
    with open("orders.txt","a") as orders_file:
        orders_file.write(order)
    
order_id = 1
ongoing_order = True
order_success = False
items_file = open("items.txt","r")
orders_file = open("orders.txt","r")
order_snippet_list = orders_file.readlines()
last_order = order_snippet_list[-1]
print(last_order[0])
if int(last_order[0]) > 0:
    order_id = int(last_order[0]) + 1   
    
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
            item = item_detail_snippet.split('    ')
            #print(item)
            #print(item[1])
            if item[0] == item_id:
                item_found = True
                if int(item[3]) >= item_qty:
                    issue_order(item, item_qty, order_id)
                    item[3] = int(item[3]) - item_qty
                    item[3] = str(item[3])
                    order_success = True
                    updated_item_detail_snippet = "    ".join(item)
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

print("Order Placed ... ")

items_file.close()