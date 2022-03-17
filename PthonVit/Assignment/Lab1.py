# # print("LAB 1")
# """Question 1
# Write a python programme to display the current date and time
# """
# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

# """Question 2
# write a python programme to get the python version you are using
# """
# import sys
# print("Python version")
# print (sys.version)
# print("Version info.")
# print (sys.version_info)

# Question 3
# """
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
# """
# a=int(input("Enter a number="))
# s=0
# for i in range(0,3):
#     s = s*10 + a
# print(s)

#  Question 4
# """
# Write a Python program to read and print various types of variables.
# """
# n = input("Enter first=")
# print(type(n))
# n1 = int(input("Enter second ="))
# print(type(n1))
# n2 = float(input("Enter Third="))
# print(type(n2))
# n3 = bool(input("Enter Fourth="))
# print(type(n3))

#  Question 5
# """
# Write a Python program to print the calendar of a given month and year.
# """
# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))

# print("LAB 2")
#  Question 1
# """
#  Python Program to Find the Square Root
# """
# number = int(input("enter a number: "))
# sqrt = number ** 0.5
# print("square root:", sqrt)

# Question 2
# """
# Python Program to Calculate the Area and Perimeter of Triangle and Circle.
# """
# n = int(input("Enter height of triangle = "))
# n1 = int(input("Enter Base of the triangle = "))
# n1_1 = int(input("Enter length of first side of triangle = "))
# n1_2 = int(input("Enter length of second side of triangle = "))
# n1_3 = int(input("Enter length of third side of triangle = "))
# n2 = int(input("Enter radius of the circle="))
# a = 0.5 * n * n1
# print("Area of triangle =", a)
# b = n1_1 + n1_3 + n1_2
# print("perimeter of triangle = ", b)
# c = 3.14 * (n2 ** 2)
# print("Area of circle = ", c)
# d = 2 * 3.14 * n2
# print("Perimeter og circle = ", d)

# Question 3
# """
# Python Program to Solve Quadratic Equation
# """
# import cmath
#
# a = 1
# b = 5
# c = 6
#
# d = (b**2) - (4*a*c)
#
# sol1 = (-b-cmath.sqrt(d))/(2*a)
# sol2 = (-b+cmath.sqrt(d))/(2*a)
#
# print('The solution are {0} and {1}'.format(sol1,sol2))

# Question 4
# """
# Python Program to Swap Two Variables
# """
# a = int(input("Enter first number="))
# b = int(input("Enter second number="))
# c = a
# a = b
# b = c
# print("After swapping")
# print("First number=", a)
# print("second number=", b)

#  Question 5
# """
# Python Program to Convert Kilometres to Miles
# """
# kilometers = float(input("Enter value in kilometers: "))
# conv_fac = 0.621371
# miles = kilometers * conv_fac
# print("Answer in miles=", miles)

#  Question 6
# """
#  Python Program to Convert Celsius To Fahrenheit
# """
# c = float(input("Enter degree Celsius = "))
# f = (c * 1.8) + 32
# print("value in fahrenheit", f)

# print("LAB 3")

#  Question 1
# """
# Python program to find whether the given number is Even or Odd
# """
# i = float(input("Enter the number ="))
# if i % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#  Question 2
# """
# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference
# """
# a = int(input('Please enter a number:'))
# d = a - 17
# if a>17:
#     s = int(2 * d)
#     print(s)
# else:
#     print(d)

# Question 3
# """
# Write a Python program to test whether a number is within 100 to 1000 or 2000 to 3000.
# """
# n = float(input("Enter the number="))
# if 100 < n < 100:
#     print("The number is between 100 to 1000")
# elif 2000 < n < 3000:
#     print("The number is between 200 to 3000")
# else:
#     print("The number is neither between 100 to 1000 nor 2000 to 3000")

#  Question 4
# """
# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum
# """
# n1 = float(input("Enter first number ="))
# n2 = float(input("Enter second number ="))
# n3 = float(input("Enter third number ="))
# if n1 == n2 == n3:
#     print(3*n1)
# else:
#     print(n1+n2+n3)

# Question 5
# """
# Python Program to Find the Factorial of a Number
# """
# p = 1
# n = int(input("Enter number = "))
# for i in range(1,n+1):
#     p = p*i
# print("Factorial of given number =", p)

# Question 6
# """
# Python Program to print maximum of 3 numbers
# """
# n1 = float(input("Enter first number= "))
# n2 = float(input("Enter second number= "))
# n3 = float(input("Enter third number= "))
# if n1 > n2:
#     b = n1
#     if b > n3:
#         print("max =", b)
#     else:
#         print("max =", n3)
# elif n2 > n1:
#     b = n2
#     if b > n3:
#         print("max =", b)
#     else:
#         print("max =", n3)
# else:
#     print("max =", n3)

# Question 7
# """
# Write a python program to find whether a given year is leap or not.
# """
# n = int(input("Enter a year ="))
# if n % 4 == 0:
#     if n % 100 == 0 and n % 400 == 0:
#         print("Leap year")
#     else:
#         print("Not a leap year")
# else:
#     print("Not a leap year")