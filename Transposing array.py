# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 17:25:10 2024

@author: Momen Hussein
"""

arr = [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]

print(list(map(list, zip(*arr))))