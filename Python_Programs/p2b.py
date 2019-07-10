#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:11:02 2019

@author: susmitvengurlekar
"""

def get_len(s):
    i = 0
    for c in s:
        i += 1
    return i

s = input("Enter string: ")
print(f"Length is: {get_len(s)}")
        
        