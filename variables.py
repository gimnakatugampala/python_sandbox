# This is a Single Line Comment

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1 #int
# y = 2.5 #float
# name = 'John' #str
# is_cool = True #boolean

# Multiple Assignment
x,y,name,is_cool = (1,2.5,'John',True)

# Basic Math
z = x+y

# Casting
x = str(x)
y = int(y)
z = float(y)


print('Hello')
print(x,y,name,is_cool)
print(z)
print(type(x))
print(type(y) ,y)
print(type(z) ,z)