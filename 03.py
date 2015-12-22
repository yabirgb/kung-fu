#! /usr/bin/env python

from __future__ import print_function

# Author: Yábir Garcia
# Email: zanklord@gmail.com
# License: GNU GPLv3

""" Write a function that tells us whether a string is a rotation of another.
You can make at most one call to the 'in' operator or to the methods index()
and find() """

import unittest

from collections import deque

def is_rotation2(word, another):
    d_object, n, lon= deque(str(word)), 0, len(word)
    while n <= lon:
        d_object.rotate(-1)
        if  ''.join(d_object) == str(another):
            return True
        n+= 1
    return False

# Segunda opcion

def findletters(string, char):
    return [i for i, letter in enumerate(string) if letter == char]

def is_rotation(word, another):
    d_object, n= deque(word), 0

    if len(word) == len(another):
        #caso de que sean vacos
        if not len(word):
            return True

        initial = another.lower()[0]
        lista = findletters(word.lower(), initial)

        for position in lista:
            d_object.rotate(-position)
            if "".join(d_object) == another:
                return True
            else:
                d_object.rotate(position)
        return False
    else:
        return False

class RotationTests(unittest.TestCase):
    def test_rotation(self):
        self.assertTrue(is_rotation("Hari Seldon","ldonHari Se"))
        self.assertTrue(is_rotation("abcdefg", "abcdefg"))
        self.assertTrue(is_rotation("abcdefg", "cdefgab"))
        self.assertTrue(is_rotation("ABCdefg", "CdefgAB"))
        self.assertTrue(is_rotation("A", "A"))
        self.assertTrue(is_rotation("abcdea","bcdeaa"))
        self.assertTrue(is_rotation("", "")) # Because reasons (see *).
        self.assertFalse(is_rotation("","A"))
        self.assertFalse(is_rotation("A","AAA"))
        self.assertFalse(is_rotation("A","B"))
        self.assertFalse(is_rotation("Hari Seldon","Hari Hari H"))
        self.assertFalse(is_rotation("abcdefg","defgABC")) # Case-sensitive
        self.assertFalse(is_rotation("abc defg","defg abc"))
        self.assertFalse(is_rotation("abc defg","defgabc")) # No space in the second sentence


	#* This one is a little tricky. It depends on your definition of "permutation". In the
        # "active" definition, as there are biyections between {} and itself ( see [1] ) then the
        # assertion is True. In the "passive" definition it could be false ( see [2] ).
        # [1] http://math.stackexchange.com/questions/140879/does-there-exist-a-bijection-between-empty-sets
        # [2] Operations on the Empty set for discussion: https://en.wikipedia.org/wiki/Empty_set


if __name__ == "__main__":
    unittest.main()
