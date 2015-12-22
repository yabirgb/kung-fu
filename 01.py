#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# Author: Yabir Garcia
# Email: zanklord@gmail.com
# License: GNU GPLv3

""" Write a function that returns whether a º has all unique characters.
For extra points, do it without using any additional data structure (such as
lists or dictionaries). You can use any function in the standard library. """

import unittest

def all_unique(word):
    if len(word) > 1:
        for letter in word.lower():
            if word.lower().count(letter) >=2:
                return False
        return True
    else:
        return True

def all_unique_dic(word):
    if len(word) > 1:
        dic = {}
        for letter in word.lower():
            if letter in dic:
                return False
            else:
                dic[letter] = 1
        return True
    else:
        return True

class AllUniqueTests(unittest.TestCase):

  def test_all_unique(self):

    self.assertTrue (all_unique_dic(""))
    self.assertTrue (all_unique_dic("a"))
    self.assertTrue (all_unique_dic("B"))
    self.assertTrue (all_unique_dic("abcde"))
    self.assertTrue (all_unique_dic("aBcDe"))
    self.assertFalse(all_unique_dic("aa"))    # Two a's
    self.assertFalse(all_unique_dic("bB"))    # Two b's (in different cases)
    self.assertFalse(all_unique_dic("abCdc")) # Two c's

if __name__ == "__main__":
    unittest.main()

