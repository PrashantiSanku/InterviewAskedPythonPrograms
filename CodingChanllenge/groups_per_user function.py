'''
The groups_per_user function receives a dictionary, which contains group names with the
list of users. Users can belong to multiple groups. Fill in the blanks to return a
dictionary with the users as keys and a list of their groups as values.
'''


def groups_per_user(group_dictionary):
    user_groups = {}

    # Go through group_dictionary to access each group and its users
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Add the group to the list of groups for this user, creating the entry if necessary
            if user not in user_groups:
                user_groups[user] = []  # Create an entry for the user if not already present
            user_groups[user].append(group)  # Add the group to the user's list of groups

    return user_groups


print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))