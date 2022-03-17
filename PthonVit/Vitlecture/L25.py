# necessary condition is number of parameter should be same to the number of argument
# it's not necessary that every parameter be used in the function(as shown down)
def q(a, b, c):
    return a + b


print(q(65, 76, 65))

print()


def run():
    for x in range(0, 10):
        if x == 2:
            return  # here return is working as break statement
        print("Run!")


run()

print()


def plus(a, b):
    s = a + b
    return s, a


s, a = plus(3, 4)
print(s, a)
# we can return multiple value from function

print()

# types of argument
print("Default Argument -->")


def p(a, b=3):
    return a + b


print(p(2))
# let if i have to modify the vale of b also
print("After modifying the value of b -->", p(65, 87))  # or p(54,b=67)

print()

# here order is important
print("Required arguments -->")


def p1(a, b):
    return a + b


print(p1(65, 76))

print()

print("Keyword argument -->")
print(p1(a=2, b=7))
# here we can change the order
print("Fter changing the order -->", p1(b=7, a=2))

print()

print("Variable number of argument -->")
"""
In case where you don't know the exact number of argument
that you want to pass to a function, you can use the following syntax with
*args
"""


def q_(*args):
    return sum(args)  # we using a built in function


print(q_(1, 2, 3, 4, 5, 6, 7, 8, 9))


def q_1(*args):
    total = 0
    for i in args:
        total = total + i  # without using built in function
    return total


print(q_1(1, 2, 3, 4, 5, 6, 4, 3, 4, 5, 6, 4, 3, 2))

print()

print("Recursion")


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\nRecursion Example Result -->")
tri_recursion(6)

print()

print("Factorial of a number using recursion -->")


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


# checking if the number is negative
num = int(input("Enter the number -->"))
if num < 0:
    print("Sorry, Factorial does not exist for negative number")
elif num == 0:
    print("The factorial of 'o' --> 1")
else:
    print("The factorial of given number -->", recur_factorial(num))

print()

"""
the variable inside the function is a local variable, means if it used outside the function
it gonna show error as 'the variable is not define'

and the variable outside the function is called global variable
"""

"""
Question -->
Write a python program to solve the Fibonacci sequence using recursion
"""


def fib(term):
    if term <= 1:
        return term
    else:
        return fib(term - 1) + fib(term - 2)


n = 10
for i in range(0, n):
    print(fib(i), end=" ")
