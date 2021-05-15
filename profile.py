import sys

currUser = sys.argv[1]


users_file = open("users.txt","r")
user_snippet_list = users_file.readlines()
for user_snippet in user_snippet_list:
    user = user_snippet.split(' ')
    if user[0] == currUser:
      print("Username : " + currUser + "\nName : " + user[1] + " " + user[2] + "\nAddress : " + " ".join(user[4:]))

choice = input("Do you wish to edit your details [Y/N] ?" )
if choice == 'Y':
    print("1. Change Password ")
    print("2. Change Address ")
    c = input("Enter Choice : ")
    users_file = open("users.txt","r")
    user_snippet_list = users_file.readlines()
    if c == '1': 
        with open("users.txt","w") as users_file:
            for user_snippet in user_snippet_list:
                user = user_snippet.split(' ')
                if user[0] == currUser:
                    new_pwd = input("Enter new password : ")
                    user[3] = new_pwd
                    updated_user = " ".join(user)
                    users_file.write(updated_user)
                    print("Password Updated successfully !! ")
                    continue
                users_file.write(user_snippet)
    elif c=='2':
        with open("users.txt","w") as users_file:
            for user_snippet in user_snippet_list:
                user = user_snippet.split(' ')
                if user[0] == currUser:
                    new_addr = input("Enter the new address : ")
                    new_addr = new_addr + "\n"
                    user[4] = new_addr
                    updated_user = " ".join(user)
                    users_file.write(updated_user)
                    print("Address Updated Successfully !!!!")
                    continue
                users_file.write(user_snippet)