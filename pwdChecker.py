import re

#input pwd string
pwd = "aswqr1234@1"

# a flag to show whether its a valid/invalid pwd
flag = 0

while True:
    #Checking all criterias
    if ((len(pwd)<6) or (len(pwd)>12)):
        print("failed", len(pwd))
        flag = -1
        break
    elif not re.search("[a-z]", pwd):
        flag = -1
        break
    elif not re.search("[0-9]", pwd):
        flag = -1
        break
    elif not re.search("[A-Z]", pwd):
        flag = -1
        break
    elif not re.search("[$#@]" , pwd):
        flag = -1
        break
    elif re.search("\s" , pwd):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break
 
if flag == -1:
    print("Not a Valid Password ")