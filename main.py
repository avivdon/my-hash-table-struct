"""MyHash

This script demonstrates the use of MyHashTable data structure, which uses a bit array and universal hashing in
order to efficiently (but inaccurately) story a key and check its existence in the hash table.
"""


import hashinterface


def get_words_from_file(filename):
    """
    Read a list of words from a given file in the required format (words are split with ',').

    :param filename: Path of file which contains words
    :return: List of strings that represent all words in the file
    """
    file = open(filename, "r")
    words = file.read().split(",")
    file.close()
    return words


def get_insertion_and_test_lists():
    """
    Ask for two file paths (one for words to be inserted and another for words to be tested),
    and create two lists with the words in each file.

    :return: insertion_words - List of strings that represent words from input file to be inserted
             tested_words    - List of strings that represent words from input file to be tested
    """

    # Ask for both file paths
    insertion_filepath = input("Get path of file which contains words for insertion: ")
    test_filepath = input("Get path of file which contains words to be tested: ")

    # Get list for both files
    insertion_words = get_words_from_file(insertion_filepath)
    tested_words = get_words_from_file(test_filepath)

    return insertion_words, tested_words


def main():

    # Initialize MyHashTable instance
    hash_table = hashinterface.init_hashtable()

    # Get words of the insertion file and words of the test file
    insertion_words, tested_words = get_insertion_and_test_lists()

    # Insert all words from the insertion file into the hash table
    hashinterface.fill_hashtable(hash_table, insertion_words)

    # Check if the given testing words are found in the hash table
    hashinterface.test_hashtable_by_words(hash_table, tested_words)


if __name__ == '__main__':
    main()
