var1="Hello World" #var1 is a string(str) type variable
var2=4 #var2 is integer(int) type variable
var3=36.7 #var3 is a floating(float) type variable
var4=" Aryan"
#type function is used to know the type of variable
print(type(var1))
"""
if we simply write type(var1), it will not print the variable type and even there will no error
but to know the type we have to use print function
so it display the type on screen
"""
print(type(var2))
print(type(var3))
print(var2+var3)
"""" if we try to add var1 and var2 , it will show error, bcz we can not add string in integer
so there is no meaning to add var1 and var2
"""
print(var1 +var4)
"""here in the above print we will not get the error
bcz we r adding string type variable to string type
"""
var5="32"
var6="45"
"""
bcz anything in double cots, variable store as string
u can see down sone example
"""
print(var1+var5)#here it will show no error bcz we r adding string in string
print(var5+var6)#here its not going to print 77, bcz here interepreter is adding two string type variable, means when two string get add they get concatinate
print(var1+var6)
#we can change any variable to other variable type using type casting
print(int(var5)+int(var6))
"""
using these fun we can typecast one variable to another
int()
float()
str()
"""
#let if i want to print something many time
print(10*"Hello world")#this will print all hello world in one line
print(10*"Hello World\n")#this will print hello world in different lines
print(100*int(var5)+int(var6))#here number will get multiply by 100,here it will not print diffrent lines but it will show matematical calculation
print(100*str(int(var5)+int(var6)))
#now we will see how to take input from user
print("Enter your number=")#we will use input function here
inpnum=input()#in inpnum, whatever user will give the input as a string inpnum will store
print("You entered=",inpnum)# if we trying to add 10 in inpnum it will show error,bcz we tring to add string in int(if instead of inpnum we write inpnum+10)
print("your modified number is=",int(inpnum)+10)#here it will print inpnum+10
print("enter first number=")
n1=input()
print("enter secound number=")
n2=input()
print("sum of two string is=",n1+n2)#here it will print n1+n2 as a strinf
print("sum of two number is=",int(n1)+int(n2))
