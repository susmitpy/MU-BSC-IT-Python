#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:21:04 2019

@author: susmitvengurlekar
"""

s = input("Enter the sentence: ")
letters = set([i.lower() for i in s if i != " "])
if len(letters) == 26:
    print("Pangram")
else:
    print("Not pangram")