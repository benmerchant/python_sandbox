# A List is a collection which is ordered and changeable. Allows duplicate members.
numbers = [1, 2, 3, 4, 5]

print(numbers)
print(type(numbers))

# using a constructor
numbers = list((5, 4, 3, 2, 1))
print(numbers)

fruits = ['Tomato', 'Pepper', 'Dragonfruit', 'Papaya', 'Cherry']

print(fruits)
print(fruits[1])

print(len(fruits))

fruits.append('Apple')
print(fruits)

fruits.remove('Pepper')
print(fruits)

# insert into position
fruits.insert(2, 'Strawberry')
print(fruits)

# remove from a position
fruits.pop(2)
print(fruits)

# reverse list
fruits.reverse()
print(fruits)

# sort list
fruits.sort()
print(fruits)

# reverse sort
fruits.sort(reverse=True)
print(fruits)
