#An example about data type conversion

num = 1
fnum = 5.0
word = "hello"

print(type(num))#classifies as an int
print(type(fnum))#classifies as a float
print(type(word))#classifies as a string

#converting an int to a string
number = 1
first_number = str(number)
second_number = type(first_number)#classifies as a string
print(second_number)

#converting string to an int
age = int(input("Enter your age: "))
print(age)#prints age as an int
