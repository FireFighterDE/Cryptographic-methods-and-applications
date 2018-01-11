#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title           : ggT.py
description     : Euklidscher Algorithmus
author          : kris
example         : python ggT.py "1" "2"
"""

import sys

def ggT(x,y):
    x = abs(int(x))
    y = abs(int(y))
    if x == 0:
        print('ggT({0},{1}): {2}'.format(sys.argv[1], sys.argv[2], y))
        return y; #Def. von Euklid
    while(y>0):
        tmp = x % y
        x = y
        y = tmp
    print('ggT({0},{1}): {2}'.format(sys.argv[1], sys.argv[2], x))
    return x;

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage {0}: x y'.format(sys.argv[0]))
        print('Parameter x: pos. oder neg. ganze Zahl.')
        print('Paranter y:  pos. oder neg. ganze Zahl.')
        sys.exit(1)
    x = sys.argv[1]
    y = sys.argv[2]
    ggT(x, y)
