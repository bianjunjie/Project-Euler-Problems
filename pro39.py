#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro39.py
# Description: 

def trangle_num(p):
    c=p/2

    n=0
    for c in range(p/2,0,-1):
	for a in range(1,c):
	    b=p-a-c
	    if b<=a and b<c and b>0 and (c*c==a*a+b*b):
		n +=1
    return n

maxS=0
for p in range(1000):
    t=trangle_num(p)
    if t>maxS:
	maxS=t
	bestp=p
print bestp

		

