# LOOP CONTROL STATEMENTS
print("CONTINUE STATEMENT -->")
# here controller will come out of the condition and returns the control to
# the loop, the loop in which 'continue statement is there'
print("PRINT ALL LETTER EXCEPT 'e' AND 's'")
# letter='VIT-AP University'
for letter in 'VIT-AP University':
    if letter == 'e' or letter == 's':
        continue
    print("Current letter :", letter)

print()

print("SKIP IF THE CURRENT NUMBER IS 6 (USING while LOOP) -->")
n = 0
while n < 10:
    n += 1
    if n == 6:
        continue
    print("current letter is=", n)

print()

print("SKIP IF THE CURRENT NUMBER IS 6 (USING 'for' LOOP) -->")
for i in range(0, 11):
    if i == 6:
        continue
    print(i)

print()

# here controller will come out of the condition in which break statement is and even
# the controller will come out of the loop in which the break statement is
# 'break', it will bring the controller out the loop
print("USING BREAK")
for j in range(0, 11):
    if j == 6:
        break
    print(j)

print()

print("-->")
for letter in 'VIT-AP university':
    if letter == 's' or letter == 'y':
        break
    print(letter)
print("current letter=", letter)

print()

print("-->")
v = 10
while v <= 10:
    if v == 6:
        break
    print(v)
    v -= 1

print()

print("-->")
v = 10
while v > 0:
    v -= 1
    if v == 6:
        continue
    print(v)

print()

print("-->")
# Exception, in this it will print 5
n = 0
while n < 10:
    print("current value=", n)
    n += 1
    if n == 5:
        continue

# Removing the problem in above syntax
# here matter where print() statement is written
n = 0
while n < 10:
    n += 1
    if n == 5:
        continue
    print("Current value=", n)

print()

print("PASS STATEMENT")
'''
PASS STATEMENT IS USED TO WRITE EMPTY LOOP.
Pass is also used for empty control statement,function and classes
'''
for letter in 'VIT-AP University':
    pass
print("last letter=", letter)  # this statement is out of loop

# skipping a letter using pass statement
for l in "VIT-AP University":
    if l == "e":
        pass
        print("this is pass block")
    print("Current letter=", l)
print("last letter =", l)

print()

print("EXAMPLE 1--> print only odd number from a list of number,using pass statement")
num = [1, 2, 3, 4, 6, 5, 7, 8, 10]
for n in num:
    if n % 2 == 0:
        pass
    else:
        print(n, "is a odd number")

print()

print("EXAMPLE 2--> Create a list of the odd number between 1 to 20(use while,break)")
n = 1
odd_num = []
while n:
    if n % 2 != 0:
        odd_num.append(n)
    if n >= 20:
        break
    n = n + 1
print("odd list=", odd_num)

print()

print("EXAMPLE 3--> Create a list of even numbers between 1 and 10(use for,while,break)")
even_list = []
for i in range(1, 11):
    while i % 2 == 0:
        even_list.append(i)
        break
print("even list=", even_list)

print()

print("""reverse a list:
a) using while loop
b) using for loop and reversed()
""")
print("using a) this is for integer list,user friendly")
n = int(input("enter the no of element u want in list="))
list1 = []
for i in range(1, n + 1):
    print("enter", i, "number =", end='')
    a = int(input())
    print()
    list1.append(a)
print(list1)
list2 = []
while n > 0:
    n = n - 1
    list2.append(list1[n])
print(list2)

print("using a) this is for String list, user friendly")
n = int(input("enter the no of element u want in list="))
list1 = []
for i in range(1, n + 1):
    print("enter", i, "string =", end='')
    a = (input())
    print()
    list1.append(a)
print(list1)
list2 = []
while n > 0:
    n = n - 1
    list2.append(list1[n])
print(list2)

wl = ['hi', 'hello', 'this', 'that', 'is', 'of']
wl1 = []
l = len(wl) - 1
while l >= 0:
    wl1.append(wl[l])
    l -= 1
print("reversed list=", wl1)

print("using b) using inbuilt function")
"""
it will not modify wl2 to reverse list, here each element will get print as it alone """
wl2 = ['hi', 'hello', 'this', 'that', 'is', 'of']
for i in reversed(wl2):
    print(i)
