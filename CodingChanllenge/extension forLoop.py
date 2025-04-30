'''
Fill in the blank using a for loop. With the given list of "filenames", this code should
rename all files with the extension .hpp to the extension .h. The code  should then
generate a new list called "new_filenames" that contains the file names with the new
extension.
You are given a list of filenames like this:

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

Output the list with all of the “.hpp” files renamed to “.h”. Leave the other filenames
alone. For this question, you must use a for loop to create the list.
'''

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new = filename.replace("hpp","h")
        new_filenames.append(new)
    else:
        new_filenames.append(filename)


print(new_filenames)

