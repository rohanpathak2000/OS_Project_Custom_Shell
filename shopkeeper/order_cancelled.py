import sys
from pathlib import Path

data_folder = Path(r"C:\Users\utkar\Documents\GitHub\OS_Project_Custom_Shell")

currUser = sys.argv[1]

from prettytable import PrettyTable

table = PrettyTable(['Order id', 'Name', 'Qty', 'Cost', 'Status', 'Transporter'])
row=[-1,-1,-1,-1,-1,-1]

curr_dir = data_folder / "customer/orders.txt"
with open(curr_dir, 'r') as items_file:
        items = items_file.readlines()
        for item in items:
                if(item.split(' ')[-2]==currUser and item.split(' ')[4]=="pending"):
                        bitem=item.split(' ')
                        length=len(bitem)
                        print(length)
                        if(length==7):
                                row[0]=bitem[0]
                                row[1]=bitem[1]
                                row[2]=bitem[2]
                                row[3]=bitem[3]
                                row[4]=bitem[4]
                                row[5]="NA"
                                table.add_row(row)
        print(table)
print("				")
print("Enter the Id of Order to be dispatched ")
item_id = input()
print("Enter the order name :")
item_name = input()
with open(curr_dir, 'w') as mater_file:
        for item in items:
                item_content = item.split(" ")
                if str(item_content[0]) == item_id  and item_content[-2]==currUser and item_content[1]==item_name:
                        if(item_content[4]=="pending"):
                                item_content[4]="cancelled"
                                join=" ".join(item_content)
                                mater_file.write(join)
                        continue
                mater_file.write(item)

