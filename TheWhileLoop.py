#An example of using a while loop in Python

count = 0
#prints out 0-9
while count < 10:
    print(count)
    count = count + 1

name = ""
while name.upper() != "STOP":
    name = input("Enter your name: ")
    print(name)
    #the loop will keep executing until I type the word STOP