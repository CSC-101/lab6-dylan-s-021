import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
# sort a list of books by title alphabetically
# input: a list of Books
# output: the given list of Books sorted by title alphabetically
def selection_sort_books(values:list[data.Book]) -> None:
    alpha_to_int = {"a":0, "A":0, "b":1, "B":1, "c":2, "C":2, "d":3, "D":3, "e":4, "E":4, "f":5, "F":5,
                    "g":6, "G":6, "h":7, "H":7, "i":8, "I":8, "j":9, "J":9, "k":10, "K":10, "l":11, "L":11,
                    "m":12, "M":12, "n":13, "N":13, "o":14, "O":14, "p":15, "P":15, "q":16, "Q":16,
                    "r":17, "R":17, "s":18, "S":18, "t":19, "T":19, "u":20, "U":20, "v":21, "V":21,
                    "w":22, "W":22, "x":23, "X":23, "y":24, "Y":24, "z":25, "Z":25}
    title_list_no_spaces = []
    for i in range(len(values) - 1):
        title_list = [values[i].title]
        title_list_no_spaces.append("".join(title_list[i].split())) # list of titles without spaces between words, ["TheHungerGames", "TheGiver"]
    title_list_int = []
    for i in range(len(values) -1):
        for t in title_list_no_spaces:
            title_list_int[i] = [alpha_to_int[l] for l in t] # list of titles with letters as numbers, [["19", "7", "4", "7", ...], ["19", "7", "4", "6", ...]]
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 2
# return a string with letters swapped case
# input: a string
# output: the input string with letters swapped case
def swap_case(string:str) -> str:
    swapped_list = []
    for l in string:
        if str.islower(l):
            swapped_list.append(str.upper(l))
        elif str.isupper(l):
            swapped_list.append(str.lower(l))
        else:
            swapped_list.append(l)
    return "".join(swapped_list)


# Part 3
# replace defined "old" characters with "new" characters in a given string
# input: 3 strings, 2 of which just 1 character
# output: a string where all the "old" characters are replaced with the "new" character
def str_translate(string:str, old:str, new:str) -> str:
    new_list = []
    for l in string:
        if l == old:
            new_list.append(new)
        else:
            new_list.append(l)
    return "".join(new_list)


# Part 4
# counting the number of times a word appears in a given string
# input: string
# output: a dictionary counting the number of times a word appears in the input string
def histogram(string:str) -> dict:
    word_list = string.split()
    word_count = {}
    for w in word_list:
        if w in word_count:
            word_count[w] = word_count[w] + 1
        else:
            word_count[w] = 1
    return word_count
