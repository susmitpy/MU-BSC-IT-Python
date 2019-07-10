#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 19:54:47 2019

@author: susmitvengurlekar
"""

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

n = int(input("Enter num: "))

print(f"Factorial is: {fact(n)}")

