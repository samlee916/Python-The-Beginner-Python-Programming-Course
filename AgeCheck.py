#This program is going to be about an age checker

count = 0
result = ""
age = 0
name = ""
#my variables

print("Welcome to the club!")
print("Please answer these questions.")
for num in range(0,3):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age >= 18:
            result = result + name + " can go inside the club.\n"
            count = count + 1
    else:
        result = name + " is not allowed in the club due to being underaged.\n"

print(result + "\n", count, "people made it into the club because they were 18 and older.")