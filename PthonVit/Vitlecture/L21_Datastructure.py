import array as ara

print("DATA STRUCTURE IN PYTHON")
print()
print("Array")
# Array is a homogeneous type of data type
print("Creating Floating Fype Array")
marks = ara.array('d', [90, 91, 92, 45, 87, 89.5, 25, 20.5])  # instead of 'd' we can also write 'f'
# printing the array
print("The marks of the students are :", end=" ")

# using for loop to access the array index
for i in range(0, 8):
    # accessing the data stored at every index by using iterator i
    print(marks[i],
          end=" ")  # here individual element of array will get print, not the entire array, here every marks is printed in floating point number
print()
print(marks)  # this will print the entire array

print()

print("Creating Integer Type Array")
marks1 = ara.array('i', [90, 91, 92, 45, 87, 89, 25, 20])
print(marks1)
for i in range(0, 4):
    print(marks1[i], end=" ")
    # printing the array(marks1) element

print()

# we can even access the one element of array without using the for loop
num = ara.array('i', [1, 2, 3, 4, 5, 6, 7, 8])
print("num=", num)
# accessing the first element of the array
print(num[0])
# accessing the second element of the array
print("num[1]=", num[1])
# we can change the value of array anytime
num[1] = 4
print("modified num[1]=", num[1])
# array get modified like list, after changing the the particular value of the array
print(num)
# a little operation
s = num[7]
y = s + 100
print(y)

print()

print("Making user defined Array-->")
b = ara.array('d', [])
n = int(input("Enter he number of element u want in array -->"))
for i in range(0, n):
    b.append(int(input("Enter number -->")))
print(b)

print()
print("Stack --> It has the system of Last-In-First-Out")
# it can store heterogeneous type of data
stack = []  # it is a type of list
'''
to perform push operation we use append()-->to access
to perform pop operation we use pop()-->to delete
top element is also called tos
'''
stack.append('a')
stack.append('b')
stack.append('c')
# stack.append(35)
print('Initial step(stack after element are append)')
print(stack)
# popping the element from the stack
print("Stack after element are popped:")
print(stack.pop())  # the last element got remove, it will print the removing element
print(stack)
stack.pop()  # the last second element got remove
print(stack)
stack.pop()  # all element got remove
# popping more than the element present, it will show error, means popping empty list will show error
print(stack)
# stack is also like a list it get modified after every operation
stack.append('m')
stack.append('2')
'''
the indexing start from topmost element, numbering started with -1
indexing can also be start from the bottom, numbering start with 0,
 like it was in list, (if we compare the indexing of stack with list, in list the
 numbering start from zero(0) from left most but in stack the numbering
 start from the bottom from zero(0) n vice - versa)
 '''
print(stack)  # stack got modified like list
print(stack[-1])
print(stack[-2])
print(stack[0])

'''
How stack is different from list?
in stack the situation is like last in first out(lifo) system

How stack is different from array?
stack can hold heterogeneous type of data, where as array can't
'''
stack.append('aryan')
stack.append('dharemendra')
print(stack)
print(stack[-4])
print(stack.pop())
print(stack)  # stack got modified
print(stack.pop())
print(stack)
stack.append('78')
stack.append('manoj')
print(stack)
stack.pop(-2)  # here the top second element get pop
print(stack)
print(stack[-1])

"""
Actually stack is a list, it getting treat as different manner if we using the 
keyword pop or append
even normal list gonna treat in different manner if we use the keyword 
pop or append
"""
