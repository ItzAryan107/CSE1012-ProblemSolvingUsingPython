# defining the function
def my_function():
    print("HELLO WORLD")


# defining the function plus
def plus(a, b):
    print("Aryan")
    return a + b


# defining minus function
def mi(a, b):
    return a - b


# defining the function multiplication
def multi(a, b):
    return a * b


# defining the function division
def div(a, b):
    return a // b  # here '//' will return integer part


# calling the function plus
print(plus(1, 2))

print()

plus(3, 4)  # called the function

print()

# making the plus function as user define
x = plus(int(input("Enter first number -->")), int(input("Enter second number -->")))
print("Summation -->", x)

print()

# calling the function
my_function()
print("\nMinus operation -->", mi(26, 7))
print("\nMultiplication operation -->", multi(34, 76.6))
print("\ndivision operation -->", div(3, 2))

print()

"""
Question -->
Write a python program to fin the max of three number
"""


# the way i thought in the class
def ma(a, b):
    if a > b:
        return a
    else:
        return b


def max2(ma, c):
    if ma > c:
        return ma
    else:
        return c


print(max2(ma(45, 56), 100))


def max_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


y = max_three(int(input("Enter First Number -->")), int(input("Enter second Number -->")),
              int(input("Enter third Number -->")))
print()
print("Max among three -->", y)
