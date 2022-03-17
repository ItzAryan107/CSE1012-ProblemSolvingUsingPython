# print("LAB 4")
# Question 1
# """ Write  a  program  which  will  find  all  such  numbers  which
#  are  divisible  by  7  but  are  not  a multiple of 5,
# between 2000 and 3200 (both included).
# The  numbers  obtained  should  be  printed  in
# a  comma-separated  sequence  on  a  single  line.
# Consider use range(#begin, #end) method
#  """
# for i in range(2000,3201):
#     if i%7==0:
#         if i % 5 != 0:
#             print(i,end=",")

# Quetion 2
# """
#  Write a python program to check whether a number is divisible by 5 and 11 or not.
# """
# n = int(input("Enter a number = "))
# if n % 5 == 0 and n % 11 == 0 :
#     print("The given number is divisible by '5' and '11' both")
# else:
#     print("number is not divisible by '5' and '11' simultaneously")

# Question 3
# """
#  Write a python program to check whether a character is alphabet or not.
# """
# ch = input("Enter a character: ")
# if (65 <= ord(ch) <= 90) or (97 <= ord(ch) <= 122):
#     print("The given character is alphabet")
# else:
#     print("it's not alphabet")

# question 4
# """
#  Write a python program to input any character and check whether it is alphabet, digit or special character.
# """
# ch1 = input("Enter=")
# if (65 <= ord(ch1) <= 90) or (97 <= ord(ch1) <= 122):
#     print("It's a character")
# elif 48 <= ord(ch1) <= 57:
#     print("The given character is digit")
# else:
#     print("The given character is special character")

# Question 5
# """
# Write a python program to check whether a character is uppercase or lowercase alphabet.
# """
# ch2 = input("Enter a alphabet=")
# if 65 <= ord(ch2) <= 90:
#     print("The given alphabet is in uppercase")
# elif 97 <= ord(ch2) <= 122:
#     print("The given alphabet is in lowercase")

# Question 6
# """
#  Write a python program to input week number and print week day.
# """
# weekday = int(input("Enter week number between 1-7= "))
# if weekday == 1 :
#     print("\nMonday");
#
# elif weekday == 2 :
#     print("\nTuesday")
#
# elif(weekday == 3) :
#     print("\nWednesday")
#
# elif(weekday == 4) :
#     print("\nThursday")
#
# elif(weekday == 5) :
#     print("\nFriday")
#
# elif(weekday == 6) :
#     print("\nSaturday")
#
# elif weekday == 7:
#     print("\nSunday")
#
# else :
#     print("\nPlease enter any weekday number (1-7)")

# Question 7
# """
# Write a python program to count total number of notes in given amount
# """
# amt = int(input("Enter Amount"))
# n2000 = n500 = n100 = n50 = n20 = n10 = n5 = 0
# while amt > 0:
#     if amt >= 2000:
#         n2000 = int(amt / 2000)
#         amt = amt - n2000 * 2000
#     elif amt >= 500:
#         n500 = int(amt / 500)
#         amt = amt - n500 * 500
#     elif amt >= 100:
#         n100 = int(amt / 100)
#         amt = amt - n100 * 100
#     elif amt >= 50:
#         n50 = int(amt / 50)
#         amt = amt - n50 * 50
#     elif amt >= 20:
#         n20 = int(amt / 20)
#         amt = amt - n20 * 20
#     elif amt >= 10:
#         n10 = int(amt / 10)
#         amt = amt - n10 * 10
#     elif amt >= 5:
#         n5 = int(amt / 5)
#         amt = amt - n5 * 5
#     else:
#         print(amt, "==This amounts r in coin")
#         amt = 0
# print("number of Notes 0f 2000=", n2000)
# print("number of Notes 0f 500=", n500)
# print("number of Notes 0f 100=", n100)
# print("number of Notes 0f 50=", n50)
# print("number of Notes 0f 20=", n20)
# print("number of Notes 0f 10=", n10)

# print("LAB 5")
# Question 1
# """
# Write a Python program to print all natural numbers from 1 to n. -using while loop
# """
# n = int(input("Enter the number = "))
# c = 0
# while n > 0:
#     c += 1
#     print(c,end=" ")
#     n -= 1
# print()

# Question 2
# """
#  Write a Python program to find sum of all odd numbers between 1 to n.
# """
# n1 = int(input("Enter the number="))
# s = 0
# for i in range(1, n1+1):
#     if i % 2 != 0:
#         s = s + i
# print("Sum of all odd number between 1 to", n1, "=", s)

# Question 3
# """
# . Write a Python program to count number of digits in a number
# """
# n2 = int(input("Enter the Number = "))
# c = 0
# while n2 > 0:
#     n2 = int(n2/10)
#     c += 1
# print("The number of digit present =", c)

# Question 4
# """
#  Write a Python program to find first and last digit of a number.
# """
# n3 = int(input("Enter the number = "))
# a = n3
# b = n3 % 10
# n3 = int(n3 / 10)
# c = 1
# while n3 > 0:
#     n3 = int(n3/10)
#     c = c * 10
# a = int(a / c)
# print("first digit =", a)
# print("last digit =", b)

# Question 5
# """
# Write a Python program to calculate sum of digits of a number
# """
# n = int(input('Enter the number='))
# s = 0
# while n>0:
#     a = n % 10
#     s = s+a
#     n = int(n/10)
# print("Sum of the digit of the given number is=", s)

# Question 6
# """
# Write a Python program to enter a number and print its reverse
# """
# n = int(input("Enter the number="))
# rev = 0
# while n > 0:
#     a = n % 10
#     rev = rev * 10 + a
#     n = int(n/10)
# print("Reverse =", rev)

# print("LAB 6")
# Question 1
# """
# Write a Python program to check whether a number is palindrome or not.
# """
# n = int(input("Enter the number="))
# temp = n
# rev = 0
# while n > 0:
#     a = n % 10
#     rev = rev * 10 + a
#     n = int(n/10)
# if temp == rev:
#     print("Palindrome")
# else:
#     print("not Palindrome")

# question 2
# """
# Write a Python program to find frequency of each digit in a given integer.
# """
# n1 = n2 = n3 = n4 = n5 = n6 = n7 = n8 = n9 = n0 = 0
# n = int(input("Enter the number = "))
# while n > 0:
#     a = n % 10
#     if a == 0:
#         n0 += 1
#     if a == 1:
#         n1 += 1
#     if a == 2:
#         n2 += 1
#     if a == 3:
#         n3 += 1
#     if a == 4:
#         n4 += 1
#     if a == 5:
#         n5 += 1
#     if a == 6:
#         n6 += 1
#     if a == 7:
#         n7 += 1
#     if a == 8:
#         n8 += 1
#     if a == 9:
#         n9 += 1
#     n = int(n/10)
# print("Frequency of 0", n0)
# print("Frequency of 1", n1)
# print("Frequency of 2", n2)
# print("Frequency of 3", n3)
# print("Frequency of 4", n4)
# print("Frequency of 5", n5)
# print("Frequency of 6", n6)
# print("Frequency of 7", n7)
# print("Frequency of 8", n8)
# print("Frequency of 9", n9)

# Question 3
# """
#  Write a Python program to print all ASCII character with their values
# """
# ch = input("Enter a character= ")
# print("ASCII of your given character =",ord(ch))

# Question 4
# """
# Write a Python program to find all factors of a number.
# """
# n = int(input("Enter a number = "))
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)


# Question 5
# """
# Write a Python program to calculate factorial of a number.
# """
# n = int(input("Enter a number= "))
# p=1
# for i in range(1, n+1):
#     p = p * i
# print("the factorial of given number=", p)

# Question 6
# """
#  Write a Python program to print all Prime numbers between 1 to n.
#  """
# n = int(input("Enter the number = "))
# for i in range(2, n + 1):
#     a = 0
#     for j in range(2, i):
#         if i % j == 0:
#             a = i
#             break
#     if a == 0:
#         print(i,end=" ")

# Question 7
# """
# Write a Python program to check whether a number is
# Armstrong number or Strong or Prime Number or Perfect number or magic number or  not
# """
# n = int(input("Enter a number = "))
# a=0
# t = n
# z = 0
# for j in range(2,n):
#     if n % j == 0:
#         a=1
#         break
# if a == 0:
#     print("The given number is prime number")
#     z = z + 1
#
#
# c = 0
# while n > 0:
#     n = int(n / 10)
#     c += 1
# s = 0
# n = t
# while n > 0:
#     b = n % 10
#     s = s + b ** c
#     n = int(n/10)
# if s == t:
#     print("The given number is a Armstrong number")
#     z = z + 1
#
# n = t
# s1 = 0
# while n > 0:
#     d = n % 10
#     p = 1
#     for k in range(1,d+1):
#         p = p * k
#     s1 = s1 + p
#     n = int(n/10)
# if s1 == t:
#     print("The given number is a strong number")
#     z = z + 1
#
# n = t
# s2 = 0
# for l in range(1, n):
#     if n % l == 0:
#         s2 = s2 + l
# if s2 == n:
#     print("The given number is Perfect number")
#     z = z + 1
#
# while n > 0:
#     s3 = 0
#     while n > 0:
#         m = n % 10
#         s3 = s3 + m
#         n = int(n/10)
#     if s3 == 1 or s3 == 0:
#         print("The given number is magical number")
#         z = z + 1
#     elif 1 <= s3 <= 9:
#         continue
#     else:
#         n = s3
#
# if z == 0:
#     print("The given number nor magical number nor strong number nor "
#           "Armstrong number nor prime number nor perfect number")

# Question 8
# """
# Write a Python program to print Fibonacci series up to n terms.
# """
# n = int(input("Enter the no of term u want of the Fibonacci series ="))
# a = 0
# b = 1
# t = a
# print(0,end=" ")
# print(1, end=" ")
# for i in range(2,n):
#     s = a + b
#     a = b
#     b = s
#     print(s, end=" ")


# print("LAB 7")
# Question 1
# """
# Write a Python Program to Find the Largest Number in a List
# """
# a = []
# n = int(input("Enter the number of input u wanna give = "))
# for i in range(0, n):
#     print("Enter", i+1 ,"Number= ", end=" ")
#     b = float(input())
#     a.append(b)
# print("The list given by you = ", a)
# b = a[0]
# for i in range(1, n):
#     if a[i] > b:
#         b = a[i]
# print("The biggest number in your given list= ",b)

# Question 2
# """
# Write a Python Program to Find the Second Largest Number in a List
# """
# l = []
# n = int(input("Enter the number of element you want to sort = "))
# for i in range(1, n + 1):
#     print("Enter the", i, "Number=", end=" ")
#     a = float(input())
#     l.append(a)
# print("your given number of list =", l)
#
#
# for j in range(0, n):
#     c = j
#     for k in range(c + 1, n):
#         a = l[c]
#         if l[c] < l[k]:
#             l[c] = l[k]
#             l[k] = a
#             # c = k
# print("sorted list = ", l)
# print("Second largest number in the list =", l[1])

# Question 3
# """
# Write a Python Program to Put Even and Odd elements in a List into Two Different Lists
# """
# l = []
# n = int(input("Enter the number of element you want to sort = "))
# for i in range(1, n + 1):
#     print("Enter the", i, "Number=", end=" ")
#     a = float(input())
#     l.append(a)
# print("your given number of list =", l)
# a = []
# b = []
# for i in range(0, n):
#     if l[i] % 2 == 0:
#         a.append(l[i])
#     else:
#         b.append(l[i])
# print("Even number list = ", a)
# print("Odd number list = ", b)

# Question 4
# """
# Write a Python Program to Merge Two Lists and Sort it
# """
# a = int(input("Enter the number of element u wanna give in list First = "))
# l1 = []
# for i in range(1, a + 1):
#     print("Enter", i, "element of list First = ", end=" ")
#     l1.append(float(input()))
# b = int(input("Enter the number of element u gonna give in list second = "))
# l2 = []
# for j in range(1, b + 1):
#     print("Enter", j, "Element of second list = ", end=" ")
#     l2.append(float(input()))
# print('Your list first =', l1)
# print("Your second list = ", l2)
# for k in range(0, b):
#     l1.append(l2[k])
# print("Merged list before sort =", l1)
#
# for l in range(0, a + b):
#     for m in range(l + 1, a + b):
#         d = l1[l]
#         if l1[l] < l1[m]:
#             l1[l] = l1[m]
#             l1[m] = d
# print("Final sorted list =",l1)

# Question 5
# """
# Write a Python Program to Sort the List According to the Second Element in Sublist
# """
# n = int(input("Enter the number of sublist u want to have in a list = "))
# l = []
#
# for i in range(0, n):
#     l.append([])  # instead we can use 'l.append(0)', then use 'l[j]=[]' in 2nd for loop
# print(l)
# for j in range(0, n):
#     # l[j]=[]
#     print("Enter the first element as string of", j + 1, "Sublist = ", end=" ")
#     l[j].append(input())
#     print("Enter the second element as number 0f", j + 1, "Sublist = ", end=" ")
#     l[j].append(float(input()))
# print(l)
#
# for k in range(0, n):
#     # c = k
#     for m in range(k + 1, n):
#         c = l[k]
#         if l[k][1] < l[m][1]:
#             l[k] = l[m]
#             l[m] = c
# print(l)

# Question 6
# """
# Write a Python Program to Find the Second Largest Number in a List Using Bubble Sort
# """
# n = int(input("Enter the number of element u want in the list = "))
# l = []
# for i in range(0, n):
#     print("Enter the", i + 1, "Element of the list = ", end=" ")
#     l.append(float(input()))
#
# # c = n - 1
# for j in range(0 , n-1):
#     for k in range(0 , n-(j+1)):
#         d = l[k]
#         if l[k] > l[k+1]:
#             l[k] = l[k+1]
#             l[k+1] = d
#         # c -= 1
# # print(l)
# print("second largest number of ur list = ",l[n-2])

# Question 7
# """
# Write a Python Program to Sort a List According to the Length of the Elements
# """
# l = []
# n = int(input("Enter the number of element u want in list = "))
# for i in range(0 , n):
#     print("Enter", i + 1 ,"Element of the list = ", end=" ")
#     l.append(input())
# for j in range(0 , n-1):
#     for k in range(0 , n-(j+1)):
#         d = l[k]
#         if len(l[k]) > len(l[k+1]):
#             l[k] = l[k+1]
#             l[k+1] = d
# print("sorted list = ", l)

# Question 8
# """
# Write a Python Program to Find the Union of two Lists
# """
# a = int(input("Enter the number of element u wanna give in list First = "))
# l1 = []
# for i in range(1, a + 1):
#     print("Enter", i, "element of list First = ", end=" ")
#     l1.append(float(input()))
# b = int(input("Enter the number of element u gonna give in list second = "))
# l2 = []
# for j in range(1, b + 1):
#     print("Enter", j, "Element of second list = ", end=" ")
#     l2.append(float(input()))
# print('Your list first =', l1)
# print("Your second list = ", l2)
#
#
# for i in range(0, b):
#     # c = 0
#     for j in range(0, a):
#         c = 0
#         if l1[j] == l2[i]:
#             break
#         else:
#             c = 1
#     if c == 1:
#         l1.append(l2[i])
# print("Union list = ", l1)

# Question 9
# """
# Write a Python Program to Find the Intersection of Two Lists
# """
# a = int(input("Enter the number of element u wanna give in list First = "))
# l1 = []
# for i in range(1, a + 1):
#     print("Enter", i, "element of list First = ", end=" ")
#     l1.append(float(input()))
# b = int(input("Enter the number of element u gonna give in list second = "))
# l2 = []
# for j in range(1, b + 1):
#     print("Enter", j, "Element of second list = ", end=" ")
#     l2.append(float(input()))
# print('Your list first =', l1)
# print("Your second list = ", l2)
#
# l3 = []
# for i in range(0, a):
#     for j in range(0, b):
#         if l1[i] == l2[j]:
#             l3.append(l1[i])
#             break
# print("Intersection of two list = ", l3)

# Question 10
# """
# Python Program to print all odd indexed elements of a list
# """
# n = int(input("Enter the number of element u want in list = "))
# l = []
# for i in range(0, n):
#     print("Enter", i + 1, "Element of list = ", end =" ")
#     l.append(input())
# print("                  list = ", l)
# l1 = []
# for k in range(0, n):
#     l1.append(k + 1)
# print("Indexing of above list = ", l1)
# print("Odd index of list = ", end=" ")
# for j in range(0, n):
#     if (j + 1) % 2 != 0:
#         print(l[j], end=" ")