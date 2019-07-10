#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 19:34:49 2019

@author: susmitvengurlekar
"""

l = int(input("Length of fibonnaci sequence: "))

print("The fibonnaci sequence is: ")

a = 0
b = 1

print(f"{a} {b}",end=" ")

for i in range(l):
    c = a+b
    print(c,end=" ")
    a = b
    b = c
