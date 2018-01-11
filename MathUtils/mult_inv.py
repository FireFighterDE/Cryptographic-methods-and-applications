#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title           : mul_inv.py
description     : Multiplikative inverse von x mod n
author          : kris
usage           : python mul_inv.py b n
example         : python mul_inv.py "1" "2"
"""

import sys

# Satz von Fermat und Euhler

def ext_ggT(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

def mult_inv(b,n):
    g, x, _ = ext_ggT(b, n)
    if g == 1:
        return x % n

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage {0}: x y'.format(sys.argv[0]))
        print('Parameter x: +- Int Zahl, deren multiplikative inverse gesucht')
        print('Paranter n: modulo n-dimension')
        sys.exit(1)
    b = sys.argv[1]
    n = sys.argv[2]
    print("mult_inv({0},{1}): {2}".format(sys.argv[1], sys.argv[2], mult_inv(int(b), int(n)))) 