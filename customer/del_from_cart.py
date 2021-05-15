def updateInItems(item_to_update, qty_to_add):
    items_file = open("../items.txt", "r")
    item_snippet_list = items_file.readlines()
    with open("../items.txt","w") as items_file:
        for item_snippet in item_snippet_list:
            item = item_snippet.split(' ')
            if item[1] == item_to_update:
                item[3] = str(int(item[3]) + int(qty_to_add))
                updated_item = " ".join(item)    
                items_file.write(updated_item)
                continue
            items_file.write(item_snippet)
    items_file.close()     

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
   else:
        print("Item removed from cart successfully !!!!!")