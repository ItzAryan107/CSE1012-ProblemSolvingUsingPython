print("'in' and 'not in' -->")
x = 30
y = 25
list_ = [10, 20, 30, 40, 50, 60]

if x not in list_:
    print("x is not present in given list")
    print("texting 2nd statement under first if")
else:
    print("x is present in given list")

if y in list_:
    print("y is present in given list")
else:
    print("y is NOT present in given list")

# out of the conditional check----it will get print always
print()
print("'is' and 'is not'")
x = 5
if type(x) is int:
    print("true")
else:
    print("false")

y = 5.2
if type(y) is not int:
    print("true")
else:
    print("false")
print()
print("Conditional Statement -->")
print("if conditional statement -->")
a = 34
if a > 90:
    print("XYZ")
    print("condition is true")  # so here it will print nothing as condition is false
if a > 10:
    print("PQRST")
    print("condition is true")

print()
print("nested if statement -->")
i = 10
if i == 10:  # First if statement
    if i < 15:  # Nested if statement will only be executed if above statement is true
        print("i is smaller than 15")
    # Will only be executed if statement above if is true
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
else:
    print("i may be greater than 15 or may be less than 15")

print()
print("if-elif-else ladder -->")
i = 20
if i == 10:
    print("i is 10")
elif i == 15:
    print("i is 15")
elif i == 20:
    print("i is 20")
else:
    print("i is not present")
print()
"""
If the annual salary of a person is Rs. 500000 or
more, s/he has to pay 20% of his salary as income tax. If the salary is in
between 400000 499999, tax is 15% of the salary. If the salary is in
between 300000 399999, then the tax is 10% of the salary. And, if the
salary is less than 300000 it is not require to pay any tax.
Write a python program to calculate the income tax based on the above
simplified tax rules.
"""
sal = int(input("please enter your annual salary"))  # here we converting the input in integer which was in string form
if sal >= 500000:
    tax = sal * 20 / 100
    print("Your tax is: ", tax)
elif 500000 > sal >= 400000:
    tax = sal * 15 / 100
    print("Your tax is: ", tax)
elif 400000 > sal >= 300000:
    tax = sal * 10 / 100
    print("Your tax is: ", tax)
else:
    print("You do not worry about income tax, tax payable is: NIL")

print()
print("Short hand if statement(it is applied when under if condition there is only one statement) -->")
i = 10
if i < 15: print("i is less than 15")

print()
print("short hand if-else statement -->")
i = 10
print("true") if (i < 15) else print("false")
print()
print("Kenneth A. Lambert - Fundamentals of Python_ First Programs, 2nd Edition")
print("Chapter --> 3")

