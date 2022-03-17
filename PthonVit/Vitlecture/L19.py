import re

print("SPECIAL CHARACTER")

print("'\A'")
txt = "The rain in spain"
# check if the string with "The": like '^' caret in metacharacter
x = re.findall("\AThe", txt)
print(x)
if x:
    print("yes, there is a match")
else:
    print("no match")

print()

print("'\\b'")
txt1 = "The rain in spain"
# check if the given character present in the beginning or end of the word or not
x1 = re.findall(r"ain\b", txt1)
print(x1)
if x1:
    print("yes")
else:
    print("no")
x_1 = re.findall(r"\bra", txt1)
print(x_1)

print()

print("'\B'")
txt2 = "Hello Aryan how are you"
# check if the given character present, but not at the end or beginning of the word
x2 = re.findall(r"ry\B", txt2)  # just opposite of '\b'
print(x2)
if x2:
    print("yes")
else:
    print("no")

print()

print("'\d'")
txt3 = "I have 67 and 56 dollar with me"
# check if the string contains any digits(numbers from 0-9)
x3 = re.findall("\d", txt3)
print(x3)
if x3:
    print("yes, there is at least one match")
else:
    print("no match")

print()

print("'\D'")
txt4 = "The rain in spain"
# it will find all the non-digit character
x4 = re.findall("\D", txt4)
print(x4)
if x4:
    print("yes")
else:
    print("No")
txt_4 = "6749363"
x_4 = re.findall("\D", txt_4)
print(x_4)
if x_4:
    print("yes")
else:
    print("No")

print()

print("'\s'")
txt5 = "The rain in spain"
# Return a match at every whitespace character
x5 = re.findall("\s", txt5)
print(x5)
if x5:
    print("yes")
else:
    print("No")

txt_5 = "Therapizing"
x_5 = re.findall("\s", txt_5)
print(x_5)
if x_5:
    print("yes")
else:
    print("No")

print()

print("'\S'")
txt6 = "Therapiz ing hell o aryan praja[ati"
# it will check all character other than space
x6 = re.findall("\S", txt6)
print(x6)
if x6:
    print("yes")
else:
    print("No")

print()

print("ALPHANUMERIC CHARACTERS --> [a-zA-Z0-9_] and all others are consider as special character")
print("'\w'")
# it use to check whether alpha numeric character is there or not
txt7 = "The rain in spain # 763"
x7 = re.findall("\w", txt7)
print(x7)
if x7:
    print("yes, there is at least one match")
else:
    print("No match")

print()

print("'\W'")
txt_7 = "The rain in spain # 763"
# it will print al character other than alphanumeric character
x_7 = re.findall("\W", txt_7)
print(x_7)
if x_7:
    print("yes, there is at least one match")
else:
    print("No match")

print()

print("'\Z'")
txt8 = "The rain in spain"
# check if the string end with given set of string or not
x8 = re.findall("spain\Z", txt8)
print(x8)
if x8:
    print("yes")
else:
    print("No")
