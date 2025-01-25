import random
print("welcome to pwd generator")
randomchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
numofpwds = int(input("Enter the num of pwds = "))
pwdlen = int(input("Enter the len of pwd = "))

print("It's your passwords:")
for x in range (numofpwds):
    pwd = ""
    for chars in range (pwdlen):
        pwd = pwd + random.choice(randomchars)
    print(pwd)
