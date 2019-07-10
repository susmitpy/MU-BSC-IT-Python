#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:13:41 2019

@author: susmitvengurlekar
"""

def histogram(nums):
    for row_length in nums:
        for _ in range(row_length):
            print("*", end = " ")
        print("")

print("Enter Numbers: ", end = " ")
nums = [int(i) for i in input().split(" ")]
histogram(nums)

        