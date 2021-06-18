# A List is a collection which is ordered and changeable. Allows duplicate members.

#Create List
numbers = [1,2,3,4,5]
fruits = ['Apples','Oranges','Grapes','Pears']

# Use a constructor
numbers2 = list((1,2,3,4,5))

# print(numbers, numbers2)
print(fruits[2])

# Get Length
print(len(fruits))

# Append List
fruits.append('Mongos')

# Remove from lists
fruits.remove('Grapes')

# Insert into position
fruits.insert(2,'Straberries')

#Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Revserse List
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)