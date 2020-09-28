# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:17:09 2020

@author: Rohith_Vemulapally
"""

def move(fr, to):
    print("Move piece from {} to {}".format(fr, to))


def solve_hanoi(n, fr, via, to):
    if n == 0:
        pass
    else:
        solve_hanoi(n-1, fr, to, via)
        move(fr, to)
        solve_hanoi(n-1, via, fr, to)
    