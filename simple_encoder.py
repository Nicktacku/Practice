import string
from collections import deque

# TODO: should turn a string into a list where it will be returned as string

word = input("Enter word to encode: ")

li = deque(word)


def encode(letter):
    MOVE = 3

    if letter == " ":
        return " "

    alphabet = list(string.ascii_letters)
    index = alphabet.index(letter) + MOVE

    if index < 52:
        return alphabet[index]
    else:
        return alphabet[52 % index]


result = list(map(encode, li))
print("".join(result))
