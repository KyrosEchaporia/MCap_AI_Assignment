# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 10:27:59 2023

@author: Kyros Echaporia
"""

nfib = int(input("Enter length of Fibonacci series: "))
num1 = 0
num2 = 1
next_number = 0
count = 1


while(count <= nfib):
    print(next_number, end=" ")
    count += 1
    num1 = num2
    num2 = next_number
    next_number = num1 + num2
print("\n")