import re

print("METACHARACTERS")

s = 'VIT-AP University: An institute for all brilliant students'
match = re.search(r'brilliant', s)
print('start index:', match.start())
print('end index:', match.end())

print()

print("\--> Backslash:")
s1 = 'VIT.AP \ University?'
# without using \
# re,search is used to find the starting and end index of a particular thing, occurring first
match1 = re.search(r'', s1)  # if more '.' would be there, still it be giving first occurred index of '.'
print(match1)
# using \
match2 = re.search(r'', s1)
print(match2)
match3 = re.search(r'\?', s1)  # ? is a metacharacter
print(match3)
match4 = re.search(r'\\', s1)
print(match4)
match5 = re.search(r'\{', s1)
print(match5)

print()

txt = "that 76 85 will be 59 dollars"
# Find all digit character:
x = re.findall('\d', txt)  # here d means digit
print(x)

print()

print("[] --> Square Brackets:")
txt1 = "The rain in spain"
# Find all LOWER CASE character alphabetically between "a" and "m"
x1 = re.findall("[a-m]", txt1)
print(x1)
x2 = re.findall("[abc]",txt1)
print(x2)

print()

print("^ --> caret")
txt2 = "hello world"
x2 = re.findall("^hello", txt2)
print(x2)
if x2:
    print("yes, the string start with 'hello'")
else:
    print("no match")

print()

print("$ --> Dollar")
# this will check whether the given string end with given character or not
txt3 = "hello planet"
x3 = re.findall("planet$", txt3)
print(x3)
if x3:
    print("the given string end with 'planet'")
else:
    print("no match")

print()

print("'.' --> Dot:")
txt4 = "hello planet"
# search for the sequence that start with "he", followed by two (any) character and then "o"
x4 = re.findall("he..o", txt4)
print(x4)

print()

print("| --> Or:")
txt5 = "The rain in spain falls mainly in the plain!"
# check if the string contains either "falls"or"stays"
x5 = re.findall("falls|stays", txt5)
print(x5)
if x5:
    print("yes, there is at least one match")
else:
    print("no match")

print()

print("? --> Question Mark:")
txt5 = "helkjo plane.t"
x5 = re.findall("he...?o", txt5)
print(x5)
x5 = re.findall("he.?o", txt5)
print(x5)

print()

print("* --> Star:")
txt6 = "hellbjo planet"
# search for a sequence that start with "he", followed by 0 or more (any) character
x6 = re.findall("he.*o", txt6)
print(x6)

print()

print("+ --> Plus:")
txt7 = "helloko planet"
# search for a sequence that start with "he", followed by 1 or more (any) character
x7 = re.findall("he.+o", txt7)
print(x7)

print()

print("{m,n} --> Braces:")  # m-->minimum, n--> maximum number of occurrence
txt8 = "hello world"
x8 = re.findall("he.{2,4}o", txt8)
print(x8)
txt9 = "helkllio world"
x9 = re.findall("he.{2,5}o", txt9)  # here 5 shows, there should be 5 character in between he and o
print(x9)

print()

print("() --> PARENTHESIS")
txt10 = "The rain in spain falls mainly in the plain!"
# check if the string either contain "falls" or "stays":
x10 = re.findall("(falls|stays) mainly", txt10)
print(x10)
if x10:
    print("yes, there is at least one match!")
else:
    print("no match")

print()

txt11 = "My name is aryan, my brother name is ashmit, hello"
x11 = re.findall("(aryan|ashmit), hello", txt11)
print(x11)
if x11:
    print("yes, it got match")
else:
    print("no match")
