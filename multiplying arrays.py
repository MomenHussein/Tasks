#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

r1 = int(input("Enter the number of rows of first array: "))
c1 = int(input("Enter the number of columns of first array: "))
r2 = int(input("Enter the number of rows of second array: "))
c2 = int(input("Enter the number of columns of second array: "))
arr1 = [[]]
arr2 = [[]]
if(c1!=r2):
    print("Sorry Invalid dimensions")
else:
    #res = np.zeros((1,r1,c2),dtype = 'int')
    res = [[0 for o in range(r1*c2)]]
    for e1 in range(r1*c1):
        number = int(input("Enter the elements of first array: "))
        arr1.append(number)
    for e2 in range(r2*c2):
        number = int(input("Enter the elements of second array: "))
        arr2.append(number)
    for i in range (r1):
        for j in range (c2):
            for k in range(r2):
                res[i][j]+= (arr1[i][k]*arr2[k][j])
            
    print(res,end='')
