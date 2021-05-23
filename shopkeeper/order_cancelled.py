import sys
from pathlib import Path

data_folder = Path("E:\Win2020-21\OS\Project")
print("enter your shop id")
shop_id=input()

if(shop_id=="sp_1"):
        curr_dir = data_folder / "customer/orders.txt"
        with open(curr_dir, 'r') as items_file:
                items = items_file.readlines()
                for item in items:
                        print(item)
        print("				")
        print("Enter the Id of Order to be dispatched ")
        item_id = input()
        with open(curr_dir, 'w') as mater_file:
                for item in items:
                        item_content = item.split(" ")
                        if str(item_content[0]) == item_id  and item_content[5]=="sp_1":
                            if(item_content[4]=="pending"):
                                item_content[4]="cancelled"
                                join=" ".join(item_content)
                                mater_file.write(join)
                            continue
                        mater_file.write(item)

elif(shop_id=="sp_2"):
        curr_dir = data_folder / "customer/orders.txt"
        with open(curr_dir, 'r') as items_file:
                items = items_file.readlines()
                for item in items:
                        print(item)
        print("				")
        print("Enter the Id of Order to be dispatched ")
        item_id = input()
        with open(curr_dir, 'w') as mater_file:
                for item in items:
                        item_content = item.split(" ")
                        if str(item_content[0]) == item_id  and item_content[5]=="sp_2":
                            if(item_content[4]=="pending"):
                                item_content[4]="cancelled"
                                join=" ".join(item_content)
                                mater_file.write(join)
                            continue
                        mater_file.write(item)