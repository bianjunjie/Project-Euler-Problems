#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro55.py
# Description: 

def isPalin(num):
    strnum=str(num)
    l=len(strnum)
    for (i,j) in enumerate(strnum):
	if j!=strnum[l-1-i]:
	    return False
    return True

def reverse_num(n):
    m=0
    while n!=0:
	l=n%10
	m=m*10+l
	n/=10
    return m

	
def isLychrel(n):
    for i in range(50):
	m=reverse_num(n)
	r=m+n
	if isPalin(r):
	    return False
	n=r
    return True

def solve():
    result=0
    for i in range(10000):
	if isLychrel(i):
	    result+=1
    
    print result

solve()
