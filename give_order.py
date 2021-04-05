ongoing_order = True
order_success = False
item_found = False
#while(ongoing_order): 
item_name = input("Enter Name of Item : ")
item_qty = int(input("Enter the qty of purchase : "))
items_file = open("items.txt","r")
item_detail_snippets_list = items_file.readlines()
with open("items.txt", "w") as items_file:
    for item_detail_snippet in item_detail_snippets_list:
        #print(item_detail_snippet)
        #item = item_detail_snippet.split(' ')jggjvvvhb
        #print(item)
        #print(item[1])
        if item[1] == item_name:
            item_found = True
            if int(item[3]) >= item_qty:
                item[3] = int(item[3]) - item_qty
                item[3] = str(item[3])
                order_success = True
                updated_item_detail_snippet = " ".join(item)
                items_file.write(updated_item_detail_snippet)
                continue      
        items_file.write(item_detail_snippet)
if order_success:
    print("Order Given !!")
else:
    if item_found == False:
        print("Item Not Found !!")
    else:
        print("Stock Unavailable !!")
items_file.close()