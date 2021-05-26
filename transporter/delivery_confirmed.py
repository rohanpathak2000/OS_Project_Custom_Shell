import sys
from pathlib import Path

data_folder = Path("E:\Win2020-21\OS\Project")

currUser = sys.argv[1]

from prettytable import PrettyTable
table = PrettyTable(['Item id','Name','Qty','Rate','Shopkeeper Id'])

def ordrw(join):
    curr_dir = data_folder / "customer/orders.txt"
    with open(curr_dir, 'r') as items_file:
        items = items_file.readlines()
    koin=join.split(" ")
    with open(curr_dir,'w') as chatter_file:
        for item in items:
            bitems=item.split(" ")
            if koin[0]==bitems[0]:
                bitems[4] = "delivered"
                join=" ".join(bitems)
                chatter_file.write(join)
                continue
            chatter_file.write(item)


new_dir = data_folder / "transporter/transp.txt"
row=[-1,-1,-1,-1,-1]
items_file = open(new_dir,"r")
item_snippet_list = items_file.readlines()
for item_snippet in item_snippet_list:
    item = item_snippet.split(' ')
    if(item[-3]==currUser):
        for i in range(0,4):
            row[i]=item[i]
        row[-1]=item[-2]
        table.add_row(row)
print(table)

print("Enter the id of the order that has been delivered")
dlvd_id=input()
with open(new_dir,'w') as dlvd_file:
    for dlvd in item_snippet_list:
        dlvd_list = dlvd.split(" ")
        if dlvd_list[0]==dlvd_id and dlvd_list[-3]==currUser:
            base_dir = data_folder / "shopkeeper/delivered.txt"
            with open(base_dir,'a') as tp_file:
                dlvd_list[4]="delivered"
                join=" ".join(dlvd_list)
                tp_file.write(join)
                ordrw(join)
            continue
        elif dlvd_list[4]=="pending":
            print("order has not been picked up yet")
        dlvd_file.write(dlvd)
                    
table.clear_rows()