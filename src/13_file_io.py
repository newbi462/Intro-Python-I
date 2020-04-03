"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

with open("foo.txt", "r") as file:
    read_data = file.read()
        # print(read_data)
    file.closed
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
import os
print(os.getcwd())

with open("src/foo.txt", "r") as file:
    read_data = file.read()
    print(read_data)
file.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open("src/bar.txt", "w") as bar_file:
    for i in range(3):
        bar_file.write("This is line %d\r\n" % (i+1))
bar_file.closed

with open("src/bar.txt", "r") as bar_file:
    read_data2 = bar_file.read()
    print(read_data2)
bar_file.closed
# watch the white space but follow the errors
