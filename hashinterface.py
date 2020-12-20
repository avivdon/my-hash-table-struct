"""Hash Interface

This module contains functions that are used to handle MyHashTable class:

    * init_hashtable - Return an initialized instance of MyHashTable object
    * fill_hashtable - Fill MyHashTable object with a given list of words
    * test_hashtable_by_words - Print existence of words from list in MyHashTable object
    * word_to_key - Convert string to unique integer key
"""

from hashtable import MyHashTable


def init_hashtable():
    """
    Initialize MyHashTable instance using given parameters from user (HashTable size, number of Hash Functions)

    :return: Initialized instance of an empty MyHashTable object
    """

    # Ask the user to give the required parameters
    num_of_bits = int(input("Enter size of HashTable (m): "))
    num_of_hash_functions = int(input("Enter amount of Hash Functions (K): "))

    return MyHashTable(num_of_bits, num_of_hash_functions)


def fill_hashtable(hash_table, words):
    """
    Fill the hash table with a given list of strings

    :param hash_table: MyHashTable instance to be filled
    :param words: List of strings to be inserted to the hash table
    """

    # Convert all given words to keys (integers)
    keys = list(map(word_to_key, words))

    # Insert each key to the hash table
    for key in keys:
        hash_table.insert(key)


def test_hashtable_by_words(hash_table, words):
    """
    Print existence of each word from a given list in a hash table

    :param hash_table: MyHashTable instance
    :param words: List of strings to be tested if they are contained in the hash table
    """
    for word in words:
        if hash_table.contains(word_to_key(word)):
            print(f'"{word}" is contained in the Hash Table')
        else:
            print(f'"{word}" is missing in the Hash Table')


def word_to_key(word):
    """
    Convert a string to a unique integer using ascii values of letters (one-to-one function)

    :param word: String to be converted (assuming each letter has ascii value from range 0-127)
    :return: Integer that represents a unique key for a given string
    """

    # Get value of each character in the given word
    ascii_values = [ord(character) for character in word]
    total_ascii_value = 0

    # Calculate ascii value of whole word as integer in base 128
    for char_index in range(len(ascii_values)):
        total_ascii_value += (ascii_values[char_index]) * (128 ** char_index)
    return total_ascii_value
