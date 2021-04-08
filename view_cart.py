
def login():
    global currUser
    flag = 0
    user_file = open("users.txt", "r")
    user_snippet_list = user_file.readlines()
    uname = input(" Username : ")
    pwd = input(" Password : ")
    for user_snippet in user_snippet_list:
        user = user_snippet.split(' ')
        if user[0] == uname:
            print(user[0])
            if user[3] == pwd+"\n":
                print(user[3])
                currUser = uname
                flag = 1
                break
    user_file.close()
    return flag

currUser = " None "
     
def register():
    flag = 1
    global currUser
    users_file = open("users.txt","r")
    user_snippet_list = users_file.readlines()
    uname = input(" Enter username : ")
    fname = input(" Enter first name : ")
    lname = input(" Enter last name : ")
    pwd = input(" Enter password : ")
    new_user = uname + " " + fname + " " + lname + " " + pwd + "\n"
    if len(user_snippet_list) > 0:
        for user_snippet in user_snippet_list:
          user = user_snippet.split(' ')
          if user[0] == uname:
            flag = 0
            break
        if flag == 0:
            print("Username already taken ")
            ch = input("Do you wish to try again ? [Y/N] ")
            if ch == 'Y':
                return register()
            else:
                return 0
        else:
            with open("users.txt","a") as users_file:
                users_file.write(new_user)
                currUser = uname
                return 1
    else:
        with open("users.txt","a") as users_file:
            users_file.write(new_user)
            currUser = uname
            return 1

print(" In order to you must be signed in. How do you wish to proceed ")
print(" 1. Already have an account ? Sign in " )
print(" 2. New User ? Register ")
choice = int(input(" Enter Choice :  "))
if choice == 1:
    session = login()
else:
    session = register()
    
if session == 1:
    print(" ----- Cart Items ----")
    orders_file = open("orders.txt","r")
    order_snippet_list = orders_file.readlines()
    for order_snippet in order_snippet_list:
        order = order_snippet.split(' ')
        if order[4] == "in_cart":
           
    