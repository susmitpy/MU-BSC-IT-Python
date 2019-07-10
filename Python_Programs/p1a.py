#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 19:23:56 2019

@author: susmitvengurlekar
"""

current_year = 2019
name = input("What's your name? ")
age = int(input("What is your age? "))

new_year = current_year + (100-age)

print(f"Hey {name}, in {new_year} you will be 100 years old")