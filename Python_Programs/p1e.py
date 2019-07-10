#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 19:40:20 2019

@author: susmitvengurlekar
"""

def armstrong(n1,l):
    n2 = sum([int(i)**l for i in n1])
    if n1 == str(n2):
        return True
    return False
    
def palindrome(n):
    if n == "".join([i for i in reversed(n)]):
        return True
    return False

na = input("Check if armstrong: ")

if armstrong(na,len(na)):
    print("Armstrong")
else:
    print("Not armstrong")

np = input("Check if palindrome: ")
if palindrome(np):
    print("Palindrome")
else:
    print("Not palindrome")



