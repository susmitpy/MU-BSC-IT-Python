#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 19:28:35 2019

@author: susmitvengurlekar
"""

import os

files = [i for i in os.listdir() if i[-3:] == ".py"]
cwd = os.getcwd()

for file in files:
    if file != "run_all.py":
        print(f"Running {file}")
        os.system(f"python3 {cwd}/{file}")
        
        