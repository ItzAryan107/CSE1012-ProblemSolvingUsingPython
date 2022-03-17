# print("LAB - 8")
# Question 1
# """
# Write a Python program to get the 4th element and 4th element from last of a tuple
# """
# a = (1, 2, 3, 'aryan', 'ashmit', 8, 'pallavi', 'arpita', 'spandhana', 'harshita')
# """
# indexing of tuple from end, start with -1 to -n
# """
# print("4th element from starting = ", a[3])
# print("4th element from end = ", a[-4])
# Question 2
# """
# Write a Python program to find the repeated items of a tuple.
# """
# a = (1, 2, 3, 2, 1, 3, 1, 4, 2, 5, 2, 1, 5, 6, 4, 'aryan', 'pallavi', 'ashmit', 2, 1, 4, 'kamini', 'pallavi', 'manoj',
#      'aryan', 'aditya', 'dhara', 'aditya', 'pallavi', 'aryan'
#      , 7, 4, 8, 0, 4, 2)
# for i in range(0,len(a)):
#     if

# Question 3
# """
# Write a Python program to check whether an element exists within a tuple
# """
# a = (1, 2, 3, 2, 1, 3, 1, 4, 2, 5, 2, 1, 5, 6, 4, 'aryan', 'pallavi', 'ashmit', 2, 1, 4, 'kamini', 'pallavi', 'manoj',
#      'aryan', 'aditya', 'dhara', 'aditya', 'pallavi', 'aryan'
#      , 7, 4, 8, 0, 4, 2)
# n = int(input("Enter '1' for number check or '2' for string check ="))
#
# c = 0
# d = 0
#
# if n == 1:
#     n2 = int(input("Enter the number u want to check whether it is there in the tuple or not ="))
#     for i in range(0, len(a)):
#         if type(a[i]) == int:
#             if a[i] == n2:
#                 c = c + 1
#                 print("yes it contain")
#                 break
#     if c == 0:
#         print("it won't contain")
# else:
#     n3 = input("Enter the string you want to check whether it is there in the tuple or not= ")
#     for i in range(0, len(a)):
#         if type(a[i]) == str:
#             if a[i] == n3:
#                 c = c + 1
#                 print("yes it contain")
#                 break
#     if c == 0:
#         print("It won't contain")

# Question 4
# """
# Write a Python program to unzip a list of tuples into individual lists.
# """
# l = [(1, 2), (3, 4), (8, 9)]
# print(list(zip(*l)))

# Question 5
# """
#  Write a Python program to replace last value of tuples in a list.
#  """
# l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# print([t[:-1] + (100,) for t in l])

# Question 6
# """
# Write a Python program to remove an empty tuple(s) from a list of tuples.
# """
# L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# L = [t for t in L if t]
# print(L)

# Question 7
# """
# Write a Python program to convert a list of tuples into a dictionary.
# """
# tuples = [('Key 1', 1), ('Key 2', 2), ('Key 3', 3), ('Key 4', 4), ('Key 5', 5)]
# result = dict(tuples)
# print(result)

# Question 8
# """
# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
# """
# from collections import Counter
#
# my_dict = {'A': 67, 'B': 23, 'C': 45,
#            'D': 56, 'E': 12, 'F': 69}
#
# k = Counter(my_dict)
#
# high = k.most_common(3)
#
# print("Initial Dictionary:")
# print(my_dict, "\n")
#
# print("Dictionary with 3 highest values:")
# print("Keys: Values")
#
# for i in high:
#     print(i[0], " :", i[1], " ")

# print("LAB - 9")
# Question - 1
"""
Write a Python function that prints out the first n rows of Pascal's triangle.
"""

# Question - 2
# """
# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
# """
# def printValues():
#     l = list()
#     for i in range(1, 21):
#         l.append(i ** 2)
#     print(l)
# printValues()

# Question - 3
# """
# Write a Python program to detect the number of local variables declared in a function
# """
# def abc():
#     x = 1
#     y = 2
#     str1= "w3resource"
#     print("Python Exercises")
#
# print(abc.__code__.co_nlocals)

# Question - 4
# """
# Write a Python program that invoke a given function after specific milliseconds.
# """
# from time import sleep
# import math
# def delay(fn, ms, *args):
#   sleep(ms / 1000)
#   return fn(*args)
# print("Square root after specific miliseconds:")
# print(delay(lambda x: math.sqrt(x), 100, 16))
# print(delay(lambda x: math.sqrt(x), 1000, 100))
# print(delay(lambda x: math.sqrt(x), 2000, 25100))

# Question - 5
# """
# Write a Python program to get the sum of a non-negative integer
# """
# def sumDigits(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sumDigits(int(n / 10))
#
# print(sumDigits(345))
# print(sumDigits(45))

# print("LAB - 10")
# Question - 1
# """
# Write a Python program to calculate the harmonic sum of n-1
# """
# def harmonic_sum(n):
#     if n < 2:
#         return 1
#     else:
#         return 1 / n + (harmonic_sum(n - 1))
#
# print(harmonic_sum(7))
# print(harmonic_sum(4))

# Question - 2
"""
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0)
"""

# Question - 3
# """
# Write a Python program to find  the greatest common divisor (gcd) of two integers using Recursion
# """
# def gcd(a,b):
#     if(b==0):
#         return a
#     else:
#         return gcd(b,a%b)
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# GCD=gcd(a,b)
# print("GCD is: ")
# print(GCD)

# Question - 4
"""
Implement any sorting algorithm using Recursion.
"""

# print("LAB - 11")
# Question - 1
"""
Write a Python Program to Replace all Occurrences of ‘a’ with ‘b’in a String. 
If ‘a’ is not present then print appropriate message. 
"""

# Question - 2
# """
# Write a Python Program to Remove the nth Index Character from a Non-Empty String
# """
#
# str = "Geeksforgeeks is fun."
# modified_str = ''
# n = 4
# for char in range(0, len(str)):
#
#     # checking if the char index is equivalent to n
#     if (char != n):
#         # append original string character
#         modified_str += str[char]
#
# print("Modified string after removing ", n, "th character ")
# print(modified_str)

# Question - 3
# """
# Write a Python Program to Detect if Two Strings are Anagrams
# """
# def check(s1, s2):
#     # the sorted strings are checked
#     if (sorted(s1) == sorted(s2)):
#         print("The strings are anagrams.")
#     else:
#         print("The strings aren't anagrams.")
#
#     # driver code
#
# s1 = "listen"
# s2 = "silent"
# check(s1, s2)

# Question - 4
# """
# Write a Python Program to Form a New String where the First Character and the Last Character have been Exchanged.
# """
# def change(string):
#     return string[-1:] + string[1:-1] + string[:1]
#
#
# string = input("Enter string:")
# print("Modified string:")
# print(change(string))

# print("LAB - 12")
# Question - 1
"""
Write a Python program to get the last part of a string before a specified character
"""

# Question - 2
# """
# Write a Python program to count the occurrences of each word in a given sentence.
# """
# def word_count(str):
#     counts = dict()
#     words = str.split()
#
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#
#     return counts
#
# print( word_count('the quick brown fox jumps over the lazy dog.'))

# Question - 3
"""
Write a Python function to insert a string in the middle of a string.
"""

# Question - 4
"""
Write a Python function to get a string made of its first three characters of a specified string.
If the length of the string is less than 3 then return the original string.
"""

# Question - 5
# """
# Write a Python program to add a prefix text to all of the lines in a string
#  """
# import textwrap
# sample_text ='''
#      Python is a widely used high-level, general-purpose, interpreted,
#      dynamic programming language. Its design philosophy emphasizes
#      code readability, and its syntax allows programmers to express
#      concepts in fewer lines of code than possible in languages such
#      as C++ or Java.
#      '''
# text_without_Indentation = textwrap.dedent(sample_text)
# wrapped = textwrap.fill(text_without_Indentation, width=50)
# wrapped += '\n\nSecond paragraph after a blank line.'
# final_result = textwrap.indent(wrapped, '> ')
# print()
# print(final_result)
# print()

# Question - 6
# """
# Write a Python program to convert a given string into a list of words.
# """
# def Convert(string):
#     li = list(string.split(" "))
#     return li
# # Driver code
# str1 = "Geeks for Geeks"
# print(Convert(str1))

