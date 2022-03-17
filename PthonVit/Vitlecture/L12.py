print("LIST-->")
list_ = ["VIT_AP UNIVERSITY", "AMRAVATI", "AP", "INDIA"]
print("list_ -->", list_)

print()

print("LIST OF LIST-->")
list1 = [["VIT_AP UNIVERSITY", "AMRAVATI"], "AP", "INDIA"]  # this is list of list
print("list1 -->", list1)
print(list1[0])
print(list1[1])
print(list1[0][0])
print(list_[-3][:7:2])
print(list1[0][0][5])  # here it will print the letter point of list of list

print()

print("TUPLE-->")
# tuple is created using parenthesis()
t = (1, 2, 3, 4, 5)
print("Tuple 't' -->", t)
print("First element of the Tuple 't' -->", t[0])
"""
How list is different from tuple?
--> tuple can't update, but list can
"""
# t[0]=34 #this line will show no assignment,means throws an error
# to create empty tuple
t1 = ()
print("Empty Tuple -->", t1)
print()
# tuple with only one element
t2 = (1)  # wrong way to declare a tuple with one element, which is going to take as a element not as tuple
print(t2)
t2 = (1,)  # right way
print(t2)
tuple_ = ("VIT", "AP")
print(tuple_)
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)  # here it's not required to put number in single or double coats
print("Type of tuple1 -->", type(tuple1))
print("tuple1 -->", tuple1)
print("7th element og the tuple1 -->", tuple1[6])
print("The element at '-2' index of the tuple1 -->", tuple1[-2])
print()
tuple2 = ("problem", "solving", "using", "python")
tuple3 = (tuple1, tuple2)
print("Tuple of tuple1 and tuple2 -->", tuple3)
print()
print("Some operations on tuple -->")
print(tuple3[1][2][4])
print(tuple3[1][1])
print()
# boolean data type means True or False
print("Boolean")
print(type(True))  # T should be capital
print()
print("SET -->")
# set is an heterogeneous type of function
set1 = set()
set2 = ("VIT", "AP", "UNIVERSITY")
print(set1)
print(set2)
print("First element of the set2 -->", set2[0])
set3 = (1, 2, "VIT", "AP", 7.56, 8.7)
print("set3 -->", set3)
print(1 in set3)
print("vit" in set1)
print()
print("DICTIONARY -->")
# it holds two value (key, value)
Dict1 = {}
Dict2 = {1: "VIT-AP", 2: "UNIVERSITY", 3: [1, 2, 3, 4, 5, 6, 7], 4: 27.376, "vit": "Aryan"}
print("dictionary2 -->", Dict2)
print("dictionary1 -->", Dict1)
print(Dict2[3][4])
print(Dict2[4])
print(Dict2[1][0:3])
print(Dict2["vit"])
print(Dict2.get("vit"))
print()
print("Arithmetic operations -->")
"""
there r 7 arithmetic operators in python
 Addition    +
 subtraction    -
 multiplication    *
 division    /
 modulus    %
 exponentiation    **
 floor division    //
 """
v1 = 10
v2 = 20
s2 = v1 + v2
s1 = v1 - v2
s3 = v1 / v2
s4 = v1 % v2
s5 = v1 ** v2
s6 = v1 // v2  # floor division will show the division but will print the integer part of the result
s7 = v1 * v2
print(s1, s2, s3, s4, s5, s6, s7)
print()
print("Comparison operator -->")
"""
we have 6 comparison operators
greater than    >
less than    <
equal to    ==
not equal to     !=
greater than or equal to    >=
less than or equal to    <=
"""
print(v1 < v2)
print(v1 == v2)
v1 += v2  # this line means v1=v1+v2(v1=30)
print(v1)
v1 -= v2  # this means v1=v1-v2(v1=10)
print(v1)
v1 /= v2  # this means v1=v1/v2
print(v1)
print()
"""
1010=10
0101=5    bitwise right shift

1010=10
0100=4   bitwise left shift
"""
print("BITWISE SHIFT -->")
x = 10
z = x << 1  # bitwise left shift
y = x >> 1  # bitwise right shift
print("Bitwise left shift -->", z, "\tBitwise right shift -->", y)
print()
print("BITWISE 'OR'/ BITWISE 'AND' -->")
x = 10
y = 12
x |= y  # can also be written as x=x|y

"""
|=   bitwise OR
&=   bitwise AND
here computation is like
1010     10
1100     12 
------
1110     14   this is only x
"""
print("BITWISE 'OR' -->", x)
x &= y  # this can be written as x=x&y
print("BITWISE 'AND' -->", x)
print()
"""
logical and operator
AND -> if both is true, result is true else false

logical or operator
OR -> if either is true then the result is true

NOT -> complement
0->1
1->0
"""
print("LOGICAL OPERATORS -->")
a = 10
b = 20
c = -11
if (b > a) or (c == b):
    print("TRUE")
if (a > b) and (b > c):
    print("YES")
else:
    print("NO")
print()
"""
bitwise NOT
~x
0 0000 1010 -> if the left most bit is 0 then it is positive number
1 0000 1010 -> if the left most bit is 1 then it is negative number

2's complement(when 1's complement is -ve )
1 0001 -> 1's complement
1 1111

2's complement(when 1's complement is +ve)
0 1101 -> 1's complement
0 0001 -> 2's complement

if the given number is +ve
then do 2's complement according to 1(1's complement also have to get done before)
if the number is -ve 
then do 2's complement according to 0(1's complement also have to get done before)

shortcut(to find 'bitwise not')
if number is +ve
add -ve with increment in number

if number is -ve
add +ve with decrement in number
"""
print("BITWISE 'NOT' -->")
a = 2001
x = ~a
print(x)
