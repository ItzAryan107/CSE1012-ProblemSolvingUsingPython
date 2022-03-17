mystr="Aryan is a good boy"#in python index start fron zero(0)
print(len(mystr))
"""
len is used to know the length of given string
like mystr is of length 19
but index no. is counted from 0 to 19
"""
print(mystr[4])#if we have to print 4th index of string
print(mystr[0:8])#let if we have to print some part of string(in which 0 index is including but 8 index is excluded part)
print(mystr[0:19])
#if we write 'print(mystr[78])' at this it will show error, bcz 78 index wont exsist
#butif we writr'print(mystr[0:78])' it will show no error, intead it will print the available mystr
print("here it will not show erroe=",mystr[0:78])
print("here it will print leaving one character=",mystr[0:5:2])
print(mystr[0:])#by default it will take like this[0:19]
print(mystr[:15])#by default it will take like this[0:15]
print(mystr[:])#by default it will take like this[0:19]
print(mystr[::])#here by default it will take like this[0:19:1]
print(mystr[::2])
print(mystr[::87])#it will print how much it can resolve(aaga se hm zero se numbering start krte h,but piche se -1 se kerte h start)
print(mystr[-4:-2])#ye string ko piche se le raha h
print(mystr[::-1])#ye string ko ulta krdega
print(mystr[-10:-17:-1])#see the printed pattern
print(mystr[-6:-13:-2])#it will resolve accordingly
print(mystr[::-2])
"""
true and false 
is the boolean character in python
"""
mystr1="Aryanisagoodboy"
print(mystr.isalnum())#.isalnum(is alph num) it gives true and false
print(mystr1.isalnum())#no space in mystr1, so it will show true
print(mystr.isalpha())
print(mystr.endswith("boy"))
print(mystr.endswith("bdy"))
print(mystr.count("a"))#it will count the no. of a present in given string
mystr2="my name is aryan"
print(mystr2.capitalize())#it will capitalize the first letter of string
print(mystr.find("is"))#it will show the starting index no. from where the given word is starting
mystr3="MY NAME IS ARYAN"
print(mystr3.lower())#it will convert the string in lower case
print(mystr.lower())
print(mystr2.upper())
print(mystr.replace("is","are"))#it will replace the word
"""
All string functions in python

Python String.capitalize()
Converts first character to Capital Letter

Python String.casefold()
converts to case folded strings

Python String.center()
Pads string with specified character

Python String.count()
returns occurrences of substring in string

Python String.encode()
returns encoded string of given string

Python String.endswith()
Checks if String Ends with the Specified Suffix

Python String.expandtabs()
Replaces Tab character With Spaces

Python String.find()
Returns the index of first occurrence of substring

Python String.format()
formats string into nicer output

Python String.format_map()
Formats the String Using Dictionary

Python String.index()
Returns Index of Substring

Python String.isalnum()
Checks Alphanumeric Character

Python String.isalpha()
Checks if All Characters are Alphabets

Python String.isdecimal()
Checks Decimal Characters

Python String.isdigit()
Checks Digit Characters

Python String.isidentifier()
Checks for Valid Identifier

Python String.islower()
Checks if all Alphabets in a String are Lowercase

Python String.isnumeric()
Checks Numeric Characters

Python String.isprintable()
Checks Printable Character

Python String.isspace()
Checks Whitespace Characters

Python String.istitle()
Checks for Titlecased String

Python String.isupper()
returns if all characters are uppercase characters

Python String.join()
Returns a Concatenated String

Python String.ljust()
returns left-justified string of given width

Python String.lower()
returns lowercased string

Python String.lstrip()
Removes Leading Characters

Python String.maketrans()
returns a translation table

Python String.partition()
Returns a Tuple

Python String.replace()
Replaces Substring Inside

Python String.rfind()
Returns the Highest Index of Substring

Python String.rindex()
Returns Highest Index of Substring

Python String.rjust()
returns right-justified string of given width

Python String.rpartition()
Returns a Tuple

Python String.rsplit()
Splits String From Right

Python String.rstrip()
Removes Trailing Characters

Python String.split()
Splits String from Left

Python String.splitlines()
Splits String at Line Boundaries

Python String.startswith()
Checks if String Starts with the Specified String

Python String.strip()
Removes Both Leading and Trailing Characters

Python String.swapcase()
swap uppercase characters to lowercase; vice versa

Python String.title()
Returns a Title Cased String

Python String.translate()
returns mapped charactered string

Python String.upper()
returns uppercased string

Python String.zfill()
Returns a Copy of The String Padded With Zeros
"""
