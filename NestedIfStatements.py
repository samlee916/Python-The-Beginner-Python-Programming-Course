#An example using nested if statements and additional operators

num = 4
if num >= 3:
    if num <= 6: #two if statements for num to meet the conditiond
        print(num)
else: #if it doesn't meet the conditions
    print("This number is not between the 3-6.")

#and operator has to meet all conditions
num = 5
if num >= 3 and num <= 6:
      print(num)
else:
     print("This number is not between the 3-6.")

#or operator only needs to meet one condition
num = 2
if num <= 2 or num >= 3:
    print(num)
else:
    print("None of the conditions were met.")