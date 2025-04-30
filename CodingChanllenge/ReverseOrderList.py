'''
Question 3
Consider the following scenario about using Python lists:

A professor gave his two assistants, Jaime and Drew, the task of keeping an attendance list of students in the order they arrive in the classroom. Drew was the first one to note which students arrived, and then Jaime took over. After the class, they each entered their lists into the computer and emailed them to the professor. The professor wants to combine the two lists into one, in the order of each student's arrival. Jaime emailed a follow-up, saying that her list is in reverse order.
Complete the code to combine the two lists into one in the order of: the contents of Drew's list, followed by Jaime’s list in reverse order, to produce an accurate list of the students as they arrived. This function should:

accept two lists through the function’s parameters;
reverse the order of “list1”;
combine the two lists so that “list2” comes first, followed by “list1”;
return the new list.
'''


def combine_lists(list1, list2):
    combined_list = []  # Initialize an empty list variable
    list1.reverse()  # Reverse the order of "list1"
    # Combine the two lists
    combined_list = list2 + list1
    return combined_list


Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]

print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']
