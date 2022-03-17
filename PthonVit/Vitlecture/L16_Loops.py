print("Complex is also a data type --- >")
print(complex(input("Enter the complex number -->")))

print()

print("WHILE LOOP -->")
"""
General syntax:
while(expression):
statement(s)
"""
c = 0
while c <= 2:
    c = c + 1
    print("Hello VIT AP ", end=" ")
    print(c)

print()

print("WHILE WITH ELSE (Advance feature of python language) -->")
"""
Syntax:
while condition:
   #executes these statements
else:
   #execute these statements
"""
str_ = input("Enter location (Ap/vellore/chennai/Bhopal) -->")
while str_ == "AP":
    print("It is VIT AP university")
    """
    #whithout break it will infinite loop,
    or we can change the str to make the condition false
    "as compiler won't come out of the loop until and unless
    the loop condition wont get false"
    """
    break
else:
    print("You r under the other university in the same brand")

print()

print("SECOND METHOD TO BREAK THE LOOP (in 'while else' looping) -->")
b = input("Enter the location (AP/vellore/chennai/Bhopal) -->")
while b == "AP":
    print("It is VIT AP university")
    b = b + "Chennai"
else:
    print("You r under the other university in the same brand")
"""
if we not using 'break' statement in 'while else loop'
in the above code, let if the condition of while get true and if we not using the 'break' statement
it will also interpret the else statement
and if the statement in while get false it will interpret just else statement
"""

print()

print("SINGLE LINE WHILE BLOCK(it can't be used as single line as while need additional break statement -->)")
"""
SYNTAX:
while conditional statement:expression
"""
c = 0
# while(c==0):print("Hello VIT AP")#here break keyword can't be used,bcz it is single line while statement
while c == 0:  # above line will not terminate, so here using multiple line conditions format
    print("HELLO VIT AP")
    break

print()

print("FOR LOOP")
"""
general syntax:
for iterator_var in sequence
statement(s)
"""
n = int(input("Enter a number="))
for i in range(0, n):  # iterating over range 0 to n-1
    print(i)

print()

# PYTHON PROGRAM TO ILLUSTRATE
# iterating over a list
print('LIST ITERATION')
l = ["VIT", "AP", "UNIVERSITY"]
for i in l:
    print(i)

print()

# ITERATING OVER A STRING
print("String Iteration")
s = "University"
for i in s:
    print(i)

print()

# Iterating over a tuple(immutable)
print("Tuple iteration")
t = ("VIT", "AP", "University")
for i in t:
    print(i)

print()

# ITERATING OVER DICTIONARY
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print(i, d[i])

print()

# NESTED LOOP
print("NESTED LOOP")
f = int(input("ENTER THE NUMBER="))
for i in range(1, f):
    # nested
    # to iterate from 1 to 10
    for j in range(1, f):
        # print multiplication
        print(i * j, end=' ')
    print()  # this print is used to change the line

print()

print("SOME PATTERN")
g = int(input("Enter a Number="))
for i in range(0, g):
    c = 0
    for j in range(0, g):
        for k in range(0, c):
            print(" ", end='')
        print("#")
        # print()
        c += 1

print()

'''List taking input from user'''
print("TAKING INPUT IN LIST FROM USER")
lst = []  # first create empty list
n = int(input("ENTER THE NUMBER OF ELEMENTS U WANT="))
# iterating till the range
for i in range(0, n):
    print("Enter", i, "Element", end="=")
    ele = int(input())
    # print()
    lst.append(ele)  # adding the elements
print(lst)

print()

print("CREATING A LIST IN LIST, WITH 2 ELEMENT IN SON LIST UNDER PARENT LIST")
lst1 = []
n1 = int(input("ENTER THE NUMBER OF SON LIST U WANT="))
for i in range(0, n1):
    print("Enter", i, "Element", end="=")
    ele1 = [int(input()), int(input())]
    print()
    lst1.append(ele1)  # adding the elements
print(lst1)

print()

print("TAKING STRING IN LIST FROM USER")
lst2 = []
n2 = int(input("ENTER THE NUMBER OF STRING U WANT IN LIST="))
for i in range(0, n2):
    print("ENTER", i, "STRING=", end="")
    ele2 = input()
    print()
    lst2.append(ele2)
print(lst2)

print()

input_string = input("Enter all family names separated by space")

family_list = input_string.split(" ")  # split string into words,it got convert in a list
# iterate a list
# here family_list variable got convert into a list
print("Printing all family member names")
for name in family_list:
    print(name)

print("Family list -->", family_list)
