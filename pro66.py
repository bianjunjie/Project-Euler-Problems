#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro66.py
# Description: see Pell's equation, http://en.wikipedia.org/wiki/Pell%27s_equation
import math
import commonFunc as cf


def is_square(n):
    m = int(math.sqrt(n))
    if m*m == n: return True
    return False


#
# Calculate a[0]+1/(a[1]+1/(a[2]+...))
def cal_fraction(a):
    if len(a)==1: 
        h,k=a[0],1
        return h,k
    hh,kk = cal_fraction(a[1:])
    h,k=kk+a[0]*hh,hh
    g = cf.GCD(h,k)
    if g>1:
        h /= g
        k /= g
    return h,k

#solve x^2-d*y^2=1
#
def solve_dio(d):
    r = cf.expand(d)
    h = r[0]
    k = r[1]
    if h*h-d*k*k==1: return h,k

    l = [r[0]]
    n = 1
    while True:
        if n==len(r): n = 1
        l.append(r[n])
        n += 1
        h,k = cal_fraction(l)
        if h*h-d*k*k==1: return h,k
    return -1,-1


max_x = -1
max_d = -1
for d in xrange(2,1000):
    if is_square(d): continue
    x,y=solve_dio(d)
    print d,x,y
    if x>max_x: 
        max_x = x
        max_d = d
print max_x, max_d

 
