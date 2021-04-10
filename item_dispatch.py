print("enter your shop id")
shop_id=input()

if(shop_id=="sp_1"):
        with open('orders.txt', 'r') as items_file:
                items = items_file.readlines()
                for item in items:
                        print(item)
        print("				")
        print("Enter the Id of Order to be dispatched ")
        item_id = input()
        with open('orders.txt', 'w') as mater_file:
                for item in items:
                        item_content = item.split(" ")
                        if str(item_content[0]) == item_id  and item_content[5]=="sp_1":
                                with open('transp.txt','a') as tp_file:
                                        item_content[4]="arriving tp_7"
                                        join=" ".join(item_content)
                                        tp_file.write(join)
                                        mater_file.write(join)
                                continue
                        mater_file.write(item)

elif(shop_id=="sp_2"):
        with open('orders.txt', 'r') as items_file:
                items = items_file.readlines()
                for item in items:
                        print(item)
        print("				")
        print("Enter the Id of Order to be dispatched ")
        item_id = input()
        with open('orders.txt', 'w') as mater_file:
                for item in items:
                        item_content = item.split(" ")
                        if str(item_content[0]) == item_id  and item_content[5]=="sp_2":
                                with open('transp2.txt','a') as tp_file:
                                        item_content[4]="arriving tp_8"
                                        join=" ".join(item_content)
                                        tp_file.write(join)
                                        mater_file.write(join)
                                continue
                        mater_file.write(item)
