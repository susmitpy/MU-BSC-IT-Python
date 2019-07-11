#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:43:58 2019

@author: susmitvengurlekar
"""

def has_common(l1,l2):
    l1 = set(l1)
    l2 = set(l2)
    if l1.intersection(l2):
        return True
    return False

print("List 1 elements: ")
l1 = [i for i in input().split(" ")]
print("List 2 elements: ")
l2 = [i for i in input().split(" ")]

print(has_common(l1,l2))