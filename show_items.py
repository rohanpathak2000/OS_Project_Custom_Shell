print(" ======== AVAILABLE ITEMS ========= ")
print("Item_id\tItem_Name\tCategory\tQty\tRate") 
items_file = open("items.txt","r")
item_snippet_list = items_file.readlines()
for item_snippet in item_snippet_list:
    item = item_snippet.split(' ')
    #print(item)
    for itm in item:
        if itm == item[-1]:
            print(itm,end="")
        else:
            print(itm + "\t",end="")
            #print("tabspace",end=" ")
        