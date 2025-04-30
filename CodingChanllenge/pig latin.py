'''
Create a function that turns text into pig latin. Pig latin is a simple text
transformation that modifies each word by:

moving the first character to the end of each word;
then appending the letters "ay" to the end of each word.

For example, python ends up as ythonpay.
'''


def pig_latin(text):
    say = ""

    words = text.split()
    for word in words:

        say += word[1:] + word[0] + 'ay' + " "

    return say


print(pig_latin("hello how are you"))
print(pig_latin("programming in python is fun"))  