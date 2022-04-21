# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Benjo'
age = 36

# Concatenate
print('Hello, I am ' + name + ', and I am ' + str(age))

# String Formatting

# Arguments by Position
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name
print('My name is {name}, and I am {age}'.format(name='Ben', age='37'))
print('My name is {name}, and I am {age}'.format(name=name, age=age))

# F-strings (only in 3.6+)
print(f'My name is {name}, and I am currently {age} years old')

# String Methods
s = 'heyooooo world  ABC'

# Capitailze first letter
print(s.capitalize())

# Capitalize all letters
print(s.upper())

# Lowercase all letters
print(s.lower())

# Swap case
print(s.swapcase())

# length
print(len(s))

# replace
print(s.replace('world', 'everyone on earth'))

# count the number of a character
sub = 'oo'
print(s.count(sub))

# starts with
print(s.startswith('hey'))

# ends with
print(s.endswith('ABC'))

# split into a list
print(s.split())

# find position
print(s.find('ABC'))

# is all alphanumeric
print(s.isalnum())

# is all alphabetic
print(s.isalpha())

# is all numeric
print(s.isnumeric())
