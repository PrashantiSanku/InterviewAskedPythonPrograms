'''
Question 6
Fill in the blanks to complete the biography_list() function. This function reads in a
list of tuples people, which contains the name, age, and profession of each person. Then,
prints the sentence "__ is _ years old and works as __."

For example, biography_list([("Ira", 30, "a Chef")]) should print:

Ira is 30 years old and works as a Chef.
'''

def biography_list(people):

    for person in people:
        name, age, profession = person
        print("{} is {} years old and works as {}.".format(name, age, profession))

biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])


