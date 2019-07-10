#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 19:56:23 2019

@author: susmitvengurlekar
"""

vowels = ["a", "e", "i", "o", "u"]
def is_vowel(c):
    if c in vowels:
        return True
    return False


c = input("Enter the character: ")
print(f"Vowel: {is_vowel(c)}")

