# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#Create turples
fruits = ('Apples','Oranges','grapes')
fruits2 = tuple(('Apples','Oranges','grapes'))

#Single Value needs trailing comma
fruits3 = (('Apples',))

#Can't change value
# fruits[0] = 'Pears'

# Delete Turple
del fruits3
# print(fruits3)

# Get length
print(len(fruits))

print(fruits, fruits2)
# print(fruits3, type(fruits3))

# A Set is a collection which is unordered and unindexed. No duplicate members.

#Create Set
fruits_set = {'Apple','Oranges','Mangoes'}

# Check if in set
print('Apple' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Remove Sets
fruits_set.remove('Grapes')

#Add duplicates
fruits_set.add('Apple')

# Clear set
# fruits_set.clear()

# Delete
# del fruits_set

print(fruits_set)