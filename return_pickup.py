print("enter your transporter id")
trp_id=int(input())

if(trp_id==7):
    with open('orders.txt','r') as dlvy_file:
        dlvy = dlvy_file.readlines()
        for deli in dlvy:
            beli=deli.split(" ")
            if beli[5]=="tp_7":
                print(deli)
    print("Enter the id of the order that has to be picked up")
    dlvd_id=input()
    with open('orders.txt','w') as dlvd_file:
        for dlvd in dlvy:
            dlvd_list = dlvd.split(" ")
            if str(dlvd_list[0])==dlvd_id and dlvd_list[4]=="return_p":
                dlvd_list[4]="returned"
                join=" ".join(dlvd_list)
                dlvd.write(join)
                continue
            elif dlvd_list[4]=="delivered":
                print("order has not been returned yet")
            dlvd_file.write(dlvd)
if(trp_id==8):
    with open('pickup.txt','r') as dlvy_file:
        dlvy = dlvy_file.readlines()
        for deli in dlvy:
            beli=deli.split(" ")
            if beli[5]=="tp_8":
                print(deli)
    print("Enter the id of the order that has to be picked up")
    dlvd_id=input()
    with open('pickup.txt','w') as dlvd_file:
        for dlvd in dlvy:
            dlvd_list = dlvd.split(" ")
            if str(dlvd_list[0])==dlvd_id and dlvd_list[4]=="return_p":
                dlvd_list[4]="returned"
                join=" ".join(dlvd_list)
                dlvd.write(join)
                continue
            elif dlvd_list[4]=="delivered":
                print("order has not been returned yet")
            dlvd_file.write(dlvd)
