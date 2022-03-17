"""
QUE--> A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
"""
print("Answer 1 -->")
a = int(input("Enter your service year="))
b = int(input("Enter your salary="))
if a > 5:
    c = b * 0.05
    print("Your bonus=", c)
else:
    print("Your bonus= Zero")
print()
"""
QUE-->Take two int value from user and print greatest among them
"""
print("Answer 2 -->")
a = int(input("Enter first number="))
b = int(input("Enter second number="))
if a > b:
    print("greatest number is=", a)
else:
    print("greatest number is=", b)
print()
"""
Que--> Take value of length and breath of a rectangle from user and check if it is square or not
"""
print("Answer 3 -->")
x = int(input("Enter length of rectangle="))
y = int(input("Enter breadth of rectangle="))
if x == y:
    print("The given rectangle is square")
else:
    print("The given rectangle is not square")
print()
"""
Que--> A shop will give discount of 10% if the cost of purchased quantity id more than 1000
Ask user for quantity
Suppose, one unit will cost 100
Judge and print total cost for user
"""
print("Answer 4 -->")
x = int(input("Enter the quantity you purchasing="))
x *= 100
if x > 1000:
    c = x * 0.01
    x -= c
    print("Your cost=", x)
else:
    print("Your coast=", x)
print()
"""
Que--> A school has following the rule of grading system
a: Below 25-----F
b: 25-45-----E
c: 45-50-----D
d: 50-60-----C
e: 60-80------B
f: Above 80----A
Ask user to enter marks and print the corresponding grade
"""
print("Answer 5 -->")
m = int(input("Enter the student marks="))
if m >= 80:
    print("Your grade= A")
elif (m >= 60) and (m < 80):
    print("Your grade= B")
elif (m >= 50) and (m < 60):
    print("Your grade= C")
elif (m >= 45) and (m < 50):
    print("Your grade= D")
elif (m >= 25) and (m < 45):
    print("Your grade= E")
else:
    print("Your grade= F")
print()
"""
Que--> Take input of age of 3 people by user and determine oldest and youngest among them.
"""
print("Answer 6 -->")
a = int(input("Enter a age="))
b = int(input("Enter b age="))
c = int(input("Enter c age="))
if a > b and a > c:
    print("Elder is a")
    if b > c:
        print("Younger is c")
    else:
        print("Younger is b")
elif b > a and b > c:
    print("Elder is b")
    if a > c:
        print("Younger is c")
    else:
        print("Younger is a")
else:
    print("Elder is c")
    if a > b:
        print("Younger is b")
    else:
        print("Younger is a")
