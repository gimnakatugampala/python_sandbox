# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create Fucntion
def sayHello(name = 'Sam'):
    print(f'Hello {name}')

# sayHello()

# Retrun values
def getSum(num1 ,num2):
    total = num1 + num2
    return total

# print(getSum(1,5))
number = getSum(1,5)

# print(number)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1,num2 : num1 +num2
# def getSum(num1,num2): return num1 + num2

print(getSum(1,6))