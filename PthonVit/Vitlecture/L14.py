print("ASCII value of 'z' -->", ord("z"))  # it will give the ASCII value of each character
print()
a = 200
b = 20
if ord("a") <= 200 and a > 100:
    print("This is true")
    print("XYZ")
else:
    print("this is false")

print()

if ord("a") == 200 and a > 100:
    print("This is true")
    print("XYZ")
else:
    print("this is false")

print()

if ord("a") == 200 or a > 100:
    print("This is true")
    print("XYZ")
else:
    print("this is false")

print()

x = a - b * 2  # here * get perform first, as it have higher priority(u can go through boadmas rule)
print("The result for(x = a - b * 2) -->", x)

"""
print("Operators According to Priority")
print()
print("'()' -->          parentheses")
print("** -->          exponent")
print("+x,-x,~x -->    unary plus,unary minus,bitwise")
print("*,/,//,% -->    multiplication, division, floor, remainder")
print("+,- -->         addition, subtraction")
print("<<,>> -->       bitwise shift operators")
print("& -->           bitwise AND")
print("^ -->           bitwise XOR")
print("! -->           bitwise OR")
print(" '""','!"',>,>=,<,<=,is,is not,in,not in--> comparisons,identity,Membership operator")
print("not -->         logical not")
print("and -->         logical and")
print("or -->          logical or")

not---> 0 --> 1
        1---> 0
"""
print()

money = 0
meal = "fruit"
if (meal == "fruit" or meal == "sandwich") and money >= 2:  # (T or f) and F
    print("lunch being delivered")  # T and F
else:  # F
    money += 200
    print("can't deliver lunch")  # therefore it printing else statement
    print("collect some money to have a meal")
    print("yes i have money now ", money)

print()

if meal == "fruit" or meal == "sandwich" and money >= 2:  # t or f and t
    print("Lunch being delivered")  # t or f
else:  # t
    print("can't deliver Lunch")

print()

print(5 * 2 // 3)  # 1--> *    2-->//
print(5 * (2 // 3))  # 1-->//   2-->*
print(5 ** 2 ** 3)
a = 20
b = 10
c = 15
d = 5
e = 0

print()

e = (a + b) * c / d
print("the value of (a+b)*c/d -->", e)
e = ((a + b) * c) / d
print("the value of ((a+b)*c)/d -->", e)
e = (a + b) * (c / d)
print("the value of (a+b)*(c/d) -->", e)
e = a + (b * c) / d
print("the value of a+(b*c)/d -->", e)
