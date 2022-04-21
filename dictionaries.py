# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# simple dict
person = {
    'first_name': 'Benjo',
    'last_name': 'Merchant',
    'age': 36
}

print(person)

# using a constructor
person2 = dict(first_name='Ben', last_name='Marchant', age=366)

print(person2)

# access value
print('My first name is: ', person['first_name'])
print('My last name is ' + person['last_name'])

# add key/value
person['phone'] = '304-867-5309'
print(person)

# get keys
print(person.keys())

# get value
print(person.values())

# make copy
person3 = person.copy()
person3['city'] = 'Pittsburgh'
print(person3)

# remove an item
del(person['age'])
print(person)

person.pop('phone')
print(person)

# clear completely
person.clear()
print(person)

# length
print('Length =', len(person2))

# list of dict
people = [person, person2, person3, {'first_name': 'Branjamin'}]
print(people)
print(people[3]['first_name'])
