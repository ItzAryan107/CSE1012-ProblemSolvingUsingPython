a = input("Enter first thing=")
b = input("enter second thing=")
# sum() function can't sum up strings
# print(sum(a,b)) , this line gonna give error
summ = a + b
print(summ)  # its adding a and b as string

print()

"""
The way to use sum() function
sum(iterable)<-- start parameter is not provided
sum(iterable,a)<-- start parameter is provided
"""
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("sum(iterable)<-- start parameter is not provided = ", sum(c))
print("sum(iterable,a)<-- start parameter is provided = ", sum(c, 70))
d = 7
e = 8
print(d**e)  # is same as d^e, same operation can also be perform using 'pow()' function
print(" using 'pow()' function -->", pow(d, e))

# we can also use multiple line in 'print()' function
print("My name is Aryan Prajapati"
      "My Brother's name is Ashmit")
# \n --> is used to change the line
print("My name is Aryan\nMy father's name is Manoj")

print()
print()
print("READ--->> Kenneth A. Lambert - Fundamentals of Python_ First Programs, 2nd Edition")
print("Chapter ---> 1")
