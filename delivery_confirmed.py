print("enter your transporter id")
trp_id=int(input())

if(trp_id==7):
    with open('transp.txt','r') as dlvy_file:
        dlvy = dlvy_file.readlines()
        for deli in dlvy:
            print(deli)
    print("Enter the id of the order that has been delivered")
    dlvd_id=input()
    with open('transp.txt','w') as dlvd_file:
        for dlvd in dlvy:
            dlvd_list = dlvd.split(" ")
            if str(dlvd_list[0])==dlvd_id and dlvd_list[4]=="arriving":
                with open('delivered.txt','a') as tp_file:
                    dlvd_list[4]="delivered"
                    join=" ".join(dlvd_list)
                    tp_file.write(join)
                continue
            elif dlvd_list[4]=="pending":
                print("order has not been picked up yet")
            dlvd_file.write(dlvd)
if(trp_id==8):
    with open('transp2.txt','r') as dlvy_file:
        dlvy = dlvy_file.readlines()
        for deli in dlvy:
            print(deli)
    print("Enter the id of the order that has been delivered")
    dlvd_id=input()
    with open('transp2.txt','w') as dlvd_file:
        for dlvd in dlvy:
            dlvd_list = dlvd.split(" ")
            if str(dlvd_list[0])==dlvd_id and dlvd_list[4]=="arriving":
                with open('delivered.txt','a') as tp_file:
                    dlvd_list[4]="delivered"
                    join=" ".join(dlvd_list)
                    tp_file.write(join)
                continue
            elif dlvd_list[4]=="pending":
                print("order has not been picked up yet")
            dlvd_file.write(dlvd)
                    
