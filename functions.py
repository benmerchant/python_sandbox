# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# create function
def sayHeyooooo(name='Ben'):
    """
    Prints 'Heyooooo' and takes name as an arg
    """
    print('Heyooooo', name)


sayHeyooooo('Benjamin')
sayHeyooooo()

# return value


def getSum(num1, num2):
    total = num1 + num2
    return total


print(getSum(42, 58))

numSum = getSum(22, 33)
print(numSum)


def addOneToNum(num):
    num += 1
    return num


num = 44443
new_num = addOneToNum(num)
print(new_num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions


def getSum1(num1, num2): return num1 + num2


print(getSum1(9, 19))


def addOneToNum1(num): return num+1


print(addOneToNum(44))
