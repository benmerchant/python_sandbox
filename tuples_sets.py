# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
fruit_tuple = ('Apple', 'Banana', 'Cucumber')
print(fruit_tuple)

# using a constructor
fruit_tuple1 = tuple(('Apple', 'Orange', 'Grape'))
print(fruit_tuple1)

# get a single value
print(fruit_tuple[1])

# single value tuples should have a trailing comma
fruit_tuple2 = ('Apple',)
print(type(fruit_tuple2))

print(len(fruit_tuple))

# delete typle
# del fruit_tuple1
# print(fruit_tuple1)
#  ^^^^^ throws


# A Set is a collection which is unordered and unindexed. No duplicate members.

# create set
fruit_set = {'Apple', 'Banana', 'Cucumber', 'Orange', 'Grape'}
print(fruit_set, type(fruit_set))

# lets attempt to add a dupe
fruit_set1 = {'Apple', 'Banana', 'Cucumber', 'Orange', 'Grape', 'Apple'}
print(fruit_set1)

# check if in set
print('Apple' in fruit_set)
print('Apples' in fruit_set)

# add to set
fruit_set.add('Cherry')
print(fruit_set)

# remove from set
fruit_set.remove('Banana')
print(fruit_set)

# clear set
fruit_set.clear()
print(fruit_set, '<--- empty set')

# delete set
# del fruit_set
# print(fruit_set) <--- throws
