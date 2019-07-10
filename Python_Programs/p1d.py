#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 19:37:49 2019

@author: susmitvengurlekar
"""
def reverse(n):
    return "".join([i for i in reversed(n)])

n = input("Enter: ")

print("Reversed: ",end=" ")

print(reverse(n))