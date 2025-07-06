#let's build a login system 
#ask for username & password 
username = input("Enter Username: ")
password = int(input ("Enter Password: "))
#check 
if username == 'admin' and password == 1234:
    print ("Access Granted ")
else:
        print("Access Denied ")