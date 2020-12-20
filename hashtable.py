"""HashTable

This module contains MyHashTable class which represents a fast but inaccurate hash table data structure.
The class uses a universal hash family and a bit array to store keys.
Each hash function is randomly generated using two constant numbers (A, B) which are used to calculate the hash value.
"""

from random import randint


class MyHashTable:
    """
    This is a Hash table data structure using universal hash family.

    Attributes:
         _bits (list of int):
            Array of bits that is used for storing the inserted words
         _size (int):
            Size of bit array
         _consts (list of tuple of 2 ints):
            List which represents different hash-functions, as each hash-function uses different
            random-generated constants
    """
    _PRIME_NUMBER = 2 ** 31 - 1

    def __init__(self, num_of_bits, num_of_functions):
        """
        The constructor for MyHashTable class.

        :param num_of_bits: The amount of bits to be used in the hash table
        :param num_of_functions: The amount of hash-functions used when storing a key or checking its existence
        """
        self._bits = [0] * num_of_bits
        self._size = num_of_bits
        self._consts = [(randint(1, self._PRIME_NUMBER - 1), randint(0, self._PRIME_NUMBER - 1)) for i in
                        range(num_of_functions)]

    def insert(self, key):
        """
        Insert a key into the hash table

        :param key: an integer key that represents a string
        """

        # Calculate bit index of key for each hash-function and turn each bit on
        for j in self._consts:
            index = self.get_hash(key, j[0], j[1])
            self._bits[index] = 1

    def contains(self, key):
        """
        Check if a key is contained in the hash table

        :param key: an integer key that represents a string
        :return: True - if key is contained, False - if key is missing
        """

        # Calculate bit index of key for each hash-function
        for j in self._consts:
            index = self.get_hash(key, j[0], j[1])

            # If bit is off, key is missing in the hash table
            if self._bits[index] == 0:
                return False

        # All bits correlated to given key are on, key is (probably) contained in the hash table
        return True

    def get_hash(self, key, a, b):
        """
        Calculate hash value of a key using specific hash function

        :param key: an integer key that represents a string
        :param a: constant parameter of specific hash function from {1, 2, ..., PRIME_NUMBER-1}
        :param b: constant parameter of specific hash function from {0, 1, ..., PRIME_NUMBER-1}
        :return: integer value that represents an index in bit array
        """
        return ((a * key + b) % self._PRIME_NUMBER) % self._size
