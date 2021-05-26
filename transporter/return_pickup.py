import sys
from pathlib import Path

data_folder = Path(r"C:\Users\utkar\Documents\GitHub\OS_Project_Custom_Shell")

currUser = sys.argv[1]

from prettytable import PrettyTable
table = PrettyTable(['Item id','Name','Qty','Rate','Shopkeeper Id'])
new_dir = data_folder / "customer/orders.txt"
row=[-1,-1,-1,-1,-1]
items_file = open(new_dir,"r")
item_snippet_list = items_file.readlines()
for item_snippet in item_snippet_list:
    item = item_snippet.split(' ')
    if(item[-3]==currUser) and item[4]=="return_p":
        for i in range(0,4):
            row[i]=item[i]
        row[-1]=item[-2]
        table.add_row(row)
print(table)
print("Enter the id of the order that has to be picked up")
dlvd_id=input()
curr_dir = data_folder / "customer/orders.txt"
with open(curr_dir,'w') as dlvd_file:
    for dlvd in item_snippet_list:
        dlvd_list = dlvd.split(" ")
        if str(dlvd_list[0])==dlvd_id and dlvd_list[4]=="return_p" and dlvd_list[-3]==currUser:
            dlvd_list[4]="returned"
            join=" ".join(dlvd_list)
            dlvd_file.write(join)
            continue
        elif dlvd_list[4]=="delivered":
            print("order has not been returned yet")
        dlvd_file.write(dlvd)
