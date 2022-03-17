n1 = 10
n2 = 20
print(n1)
# we can not start variable name with number like(1n)
# but we can give some symbol in between like(n_1)
n_1 = 22
print(n_1)
website1 = "www.google.com"
website2 = "www.yahoo.com"
print(website1)
website1 = "www.vitap.com"
print(website1)  # now in website1 something else is there....downward it will continue with modified website1
x, y, z = 10.5, "hello world", 200
print(x, end="")
print("\t", y, end="")  # '\t' is used to generate a tab gap
print("\t", z)
p = q = r = 500  # in p,q,r have value same,we can see down
print(p, end="")
print("\t", q, end="")
print("\t", r)
from Vitlecture import constants

print("(from new file) PI=", constants.PI)
print("(from constanta file) GRAVITY=", constants.GRAVITY)
# literal is a raw data given in a variable or constant
n1 = 10  # decimal form
n2 = 0b10101  # binary form
n3 = 0o310  # octal form
n4 = 0x12c  # hexadecimal form
print("Decimal form-->", n1, "\tbinary to decimal-->", n2, "\toctal to decimal-->", n3, "\thexa to decimal-->",
      n4)  # result will come in decimal form
float1 = 19.5
print(float1)
print(type(float1))
print(type(n1))
# compile literal, here iota=j z=x+jy
x = 3.34j  # here real part is 0 and imaginary part is 3.34
print(x.imag)
print(x.real)
y = 34 + 78j
print(y.real)
print(y.imag)
print(type(y))
# whatever sir taught about string in this lecture,u can see all in pythontuts/tut8
print(y)
string1 = "Hello World"
print("Length of String1 -->", len(string1))
# Indexing of string start from 0(zero) to (len(string)-1)
# reversing indexing is also there in python, here indexing start from the last of the string with '-1'
print(string1[-1])  # here it will print 'd' as at last 'd' is there of the string

# printing string1 in reverse order using for loop
for i in range(-1, -(len(string1) + 1), -1):
    print(string1[i])
