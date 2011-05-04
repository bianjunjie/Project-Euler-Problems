#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro44.py
# Description: 
import math
def isPentagonal(num):
    t=int(math.sqrt(1+24*num))
    t=int((1+t)/6.)
    if 3*t*t-t==2*num:
	return True
    return False

def pentagnal(n):
    return n*(3*n-1)/2

def solve():
    PenList=[]
    i=0
    while True:
	i+=1
	p=pentagnal(i)
	for j in PenList:
	    if isPentagonal(abs(p-j)) and isPentagonal(p+j):
		print abs(p-j)
		return
	
	PenList.append(p)

solve()
