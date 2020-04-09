"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated.

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [x+1 for x in range(5)]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [x**3 for x in range(10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [x.upper() for x in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

#def is_even(*passed):
#    for i in passed:
#        hold = passed
#        return hold[1]
#  if int(passed) % 2 == 0:
#      return passed
hold = []
for i in x:
    if int(i) % 2 == 0:
        #print(i)
        hold.append(i)
# more one line

"""
new_list = []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))
You can obtain the same thing using list comprehension:
new_list = [expression(i) for i in old_list if filter(i)]
"""

# What do you need between the square brackets to make it work?
# y = [*hold]
y = [i for i in x if int(i) % 2 == 0]
# even as in "2" or as in [0]?

print(y)
