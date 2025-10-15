# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 16:56:11 2025

@author: emiil
"""

weight = input("Weight: " )
unit = input("(K)g or (L)bs: " )
if unit.upper() == "L":
    print("Weight in Kg: ", float(weight)/2.25)
else:
    print("Weight in Lbs: ", float(weight)*2.25)
