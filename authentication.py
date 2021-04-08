import subprocess

def login(username, pwd):
    user_file = open("users.txt", "r")
    user_snippet_list = user_file.readlines()
    for user_snippet in user_snippet_list:
        user = user_snippet.split(' ')
        if user[0] == username:
            if user[1] == pwd:
                user_file.close()
                return 1
    user_file.close()
    return 0 
     
check = 0

while(check == 0):
    name = input("Name : ")
    pwd = input("Password : ")
    check = login(name,pwd)
    if check == 1:
        subprocess.call("./consumer_home_page.sh")
    