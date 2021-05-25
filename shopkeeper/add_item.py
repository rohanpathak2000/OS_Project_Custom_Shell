import sys
from pathlib import Path

data_folder = Path("E:\Win2020-21\OS\Project")
print("enter your shop id")
shop_id=input()

if(shop_id=="sp_1"):
        curr_dir = data_folder / "items.txt"
        with open(curr_dir, 'r') as items_file:
                items = items_file.readlines()
                last_item_id=int(items[-1].split(' ')[0])
        temp=[-1,-1,-1,-1,-1]
        temp[0]=str(last_item_id+1) 
        print("Enter the name of Item ")
        item_name = input()
        temp[1]=item_name
        print("Enter the price of Item ")
        item_price = input()
        temp[2]='fruits'
        temp[3]=str(item_price)
        print("Enter the qty of Item ")
        item_qty = input()
        temp[4]=str(item_qty+"\n")
        with open(curr_dir, 'a') as mater_file:
                join=" ".join(temp)
                mater_file.write(join)

if(shop_id=="sp_2"):
        curr_dir = data_folder / "items.txt"
        with open(curr_dir, 'r') as items_file:
                items = items_file.readlines()
                last_item_id=int(items[-1].split(' ')[0])
        temp=[-1,-1,-1,-1,-1]
        temp[0]=str(last_item_id+1)
        print("Enter the name of Item ")
        item_name = input()
        temp[1]=item_name
        print("Enter the price of Item ")
        item_price = input()
        temp[2]="dairy"
        temp[3]=item_price
        print("Enter the qty of Item ")
        item_qty = input()
        temp[4]=str(item_qty+"\n")
        with open(curr_dir, 'a') as mater_file:
                join=" ".join(temp)
                mater_file.write(join)