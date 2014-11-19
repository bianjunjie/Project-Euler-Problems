#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: commonFunc.py
# Description: 

import math
from datetime import *
'''
Check if a number is  a palindromic number
'''
def isPali(num):
    n=str(num)
    while len(n)>1:
	if n[0]!=n[-1]:
	    return False
	n=n[1:-1]
    return True


'''
Expand to continous fration representation
'''
#
#\frac{c}{sqrt(a) - b}
def getnext(a,b,c):
    real =int( c/(math.sqrt(a)-b) )
    new_a = a
    new_b = (b*c-real*(a-b*b))/c *-1
    new_c = (a-b*b)/c
    return real,new_a,new_b,new_c

def expand(n):
    r=[]
    real = int(math.sqrt(n))
    r.append(real)
    a = n
    b = real
    c = 1
    loop = [[a,b,c]]
    while True:
        real,new_a,new_b,new_c = getnext(a,b,c)
        r.append(real)
        loop.append([new_a,new_b,new_c])
        found = False
        for val in loop[:-1]:
            if new_a==val[0] and new_b==val[1] and new_c==val[2]:
                found = True
                break
        if found: break
        a = new_a
        b = new_b
        c = new_c
    return r


def GCD(x,y):
    if x==1 or y==1: return 1
    if x==y: return x
    if x>y: return GCD(y,x)
    if y%x==0: return x
    return GCD(y%x, x)
    
def timeit(func):
    def inner(*args,**kargs):
        start = datetime.now()
        ret = func(*args, **kargs)
        end = datetime.now()
        print "time cost: ", end - start
        return ret
    return inner
