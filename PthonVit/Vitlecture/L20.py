import re

print("SETS")
print("FIRST WAY")
txt = "The rain in spain"
# check if the string has any given character or not
x = re.findall("[arn]", txt)
print(x)  # here x is like list
if x:
    print("yes")
else:
    print("No")

print()

print("SECOND WAY")
x1 = re.findall("[a-n]", txt)  # here only lower case will get print
print(x1)
if x1:
    print("yes")
else:
    print("No")

print()

print("THIRD WAY")
x2 = re.findall("[^arn]", txt)
# check if the string have any other character other than given characters
print(x2)
if x2:
    print("Yes")
else :
    print("No")

print()

print("FOURTH WAY")
txt1 = "My name is aryan, 10/07/2002"
x3 = re.findall("[0-3]", txt1)  # it will print 0-3 all number if present in the string
print(x3)

print()

print("FIFTH WAY")
txt2 = "123456789"
x4 = re.findall("[^0-4]", txt2)
print(x4)  # it will print all character leaving 0-4

print()

print("SIXTH WAY")
txt3 = "12 384 73 65 37 86 54 76 49 2 60"
# check if the string has any two digit number,where range of first digit id[012345] and range of second digit[987654]
x5 = re.findall("[012345][987654]", txt3)  # the same way we can do for three digit
print(x5)

print()

print("SEVENTH WAY")
txt4 = "my name is ARYAN, ///,.<> Prajapati"
x6 = re.findall("[a-pA-R]", txt4)
# check if the string have any character from a-p lower case and A-R upper case
print(x6)

print()

txt5 = "it's time + $. to rookkk"
x7 = re.findall("[+]", txt5)  # in the same way we can check all other special character
# check if the string have any special character or not
print(x7)

print()

print("findall")
# it find all the list containing all matches
txt8 = "The rain in spain"
x6 = re.findall("ai", txt8)
print(x6)
# if no match found it return nul list or empty list

print()

print("search()")
# it will find the very first occurrence
txt9 = "the rain in spain"
x7 = re.search("\s", txt9)  # it find the first white space, or we can use for any character
print(x7)
x8 = re.search("v", txt9)
print(x8)  # it will return none

print()

print("split()")
txt10 = "The rain in spain"
x9 = re.split("\s", txt10)
print(x9)  # separated as a list
x10 = re.split("i", txt10)  # at the place of i it will create separate element of list
print(x10)
x_10 = re.split("i", txt10, 1)
'''
here it will make the separate(split) element in list just at first i,
if instead of 1 it would be 2 then it be creating element at 2 i,
if the splitting range is greater than it's limit then it go to it's
maximum how much it can split
'''
print(x_10)

print()

print("sub()")
# means substitute,or replacing
txt11 = " The rain in spain "
x11 = re.sub(" ", "//", txt11)
print(x11)
x_11 = re.sub(" ", "?", txt11,3)
# here we given the max range, how much white space will get replace or substitute
print(x_11)

print()

print("Kenneth A. Lambert - Fundamentals of Python_ First Programs, 2nd Edition")