# Strings and String Methods Assignment
# In the Python shell (IDLE), PyCharm, or Jupyter Notebook, play with lists. Reference: https://docs.python.org/3/tutorial/datastructures.html
# Assign a string of your favorite movie character and the movie they are in to a variable. For example, "Carol Danvers in Captain Marvel".
# Next, one by one, use each of the methods and print the result. NOTE: You may need to use a substring or character to display the method use correctly.
# capitalize
# find
# index
# isalnum
# isalpha
# isdigit
# islower
# isupper
# isspace
# startswith
# Take a screenshot of 2 at a time and submit 5 screenshots.

movChar = 'jack burton in big trouble in little china'

x = movChar.split()

print(x)

for i in range(len(x)):
    x[i] = x[i].capitalize()

newVar = ''
for i in range(len(x)):
    newVar = newVar + ' ' + x[i]

print(x)

print('capitalize: ' + newVar)
print('find: ' + str(movChar.find('in')))
print('index: ' + str(movChar.index('u')))
print('isalnum: ' + str(movChar.isalnum()))
print('isalpha: ' + str(movChar.isalpha()))
print('isdigit: ' + str(movChar.isdigit()))
print('islower: ' + str(movChar.islower()))
print('isupper: ' + str(movChar.isupper()))
print('isspace: ' + str(movChar.isspace()))
print('startswith: ' + str(movChar.startswith('j')))





