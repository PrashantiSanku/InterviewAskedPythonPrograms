'''
Question 2
Fill in the blank using a list comprehension. With the given list of "filenames", this
code should rename all files with the extension .hpp to the extension .h. The code
function should then generate a new list called "new_filenames" that contains the
filenames with the new extension.

You are given a list of filenames like this:

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

Output the list with all of the “.hpp” files renamed to “.h”. Leave the other filenames
alone. For this question, you must use list comprehension to create the list.
'''


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

# Use list comprehension to rename .hpp to .h
new_filenames = [filename.replace(".hpp", ".h") if filename.endswith(".hpp") else filename for filename in filenames]

print(new_filenames)