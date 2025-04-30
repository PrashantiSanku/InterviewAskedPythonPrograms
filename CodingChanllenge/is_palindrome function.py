'''
Fill in the blanks to complete the is_palindrome function. This function checks if a given
string is a palindrome. A palindrome is a string that contains the same letters in the
same order, whether the word is read from left to right or right to left. Examples of
palindromes are words like kayak and radar, and phrases like "Never Odd or Even".
The function should ignore blank spaces and capitalization when checking if the given
string is a palindrome. Complete this function to return True if the passed string is a
palindrome, False if not.

'''


def is_palindrome(input_string):

    new_string = ""
    reverse_string = ""

    for letter in input_string:

        if letter != " ":

            new_string = new_string + letter.lower()
            reverse_string = letter.lower() + reverse_string


    if new_string == reverse_string:

        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True