#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:21:04 2019

@author: susmitvengurlekar
"""

def is_panagram(s):
    letters = set([i.lower() for i in s if i != " "])
    if len(letters) == 26:
        return True
    return False

    

s = input("Enter the sentence: ")
if is_panagram(s):
    print("Pangram")
else:
    print("Not pangram")