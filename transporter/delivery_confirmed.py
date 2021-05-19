import sys
from pathlib import Path

data_folder = Path("E:\Win2020-21\OS\Project")
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

print("enter your transporter id")
trp_id=int(input())

if(trp_id==7):
    new_dir = data_folder / "transporter/transp.txt"
    with open(new_dir,'r') as dlvy_file:
        dlvy = dlvy_file.readlines()
        for deli in dlvy:
            print(deli)
    print("Enter the id of the order that has been delivered")
    dlvd_id=input()
    with open(new_dir,'w') as dlvd_file:
        for dlvd in dlvy:
            dlvd_list = dlvd.split(" ")
            if str(dlvd_list[0])==dlvd_id and dlvd_list[4]=="arriving":
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
if(trp_id==8):
    new_dir = data_folder / "transporter/transp2.txt"
    with open(new_dir,'r') as dlvy_file:
        dlvy = dlvy_file.readlines()
        for deli in dlvy:
            print(deli)
    print("Enter the id of the order that has been delivered")
    dlvd_id=input()
    with open(new_dir,'w') as dlvd_file:
        for dlvd in dlvy:
            dlvd_list = dlvd.split(" ")
            if str(dlvd_list[0])==dlvd_id and dlvd_list[4]=="arriving":
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
                    
