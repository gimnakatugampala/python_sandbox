# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#Create Class
class User:
    #Constructor
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age

    #fucntion
    def greeting(self):
        return f'My name is {self.name} am I am {self.age}'

    def has_birthday(self):
        self.age += 1

#Extend Classes
class Customer(User):
    #Custructor
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self,balance):
        self.balance = balance
    
    def greeting(self):
        return f'My name is {self.name} am I am {self.age} and my balance is {self.balance}'
        
        

#Init user object
brad = User('Brad Traversy','brad@gmail.com',33)

#Init cusomter object
janet = Customer('Janet Jackson','janet@gmail.com',45)

janet.set_balance(500)
print(janet.greeting())
    
# print(type(brad))
# print(brad.name)
brad.has_birthday()
print(brad.greeting())