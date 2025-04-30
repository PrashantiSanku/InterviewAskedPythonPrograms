'''
Consider the following scenario about using Python dictionaries and lists:

Tessa and Rick are hosting a party. Before they send out invitations, they want to add all of the people they are inviting to a dictionary so they can also add how many guests each friend is bringing to the party.

Complete the function so that it accepts a list of people, then iterates over the list and adds all of the names (elements) to the dictionary as keys with a starting value of 0. Tessa and Rick plan to update these values with the number of guests their friends will bring with them to the party. Then, print the new dictionary.

This function should:

accept a list variable named “guest_list” through the function’s parameter;

add the contents of the list as keys to a new, blank dictionary;

assign each new key with the value 0;

print the new dictionary.
'''

def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = {} # Initialize a new dictionary
    for guest in guest_list: # Iterate over the elements in the list
        result[guest] = 0 # Add each list element to the dictionary as a key with
            # the starting value of 0
    return result

guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]

print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}