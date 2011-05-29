#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro56.py
# Description: 


def sumdigit(n):
    r=0
    while n>0:
	r=r+n%10
	n/=10
    return r

def solve():
    max_sum=-1
    for a in range(1,100):
	for b in range(1,100):
	    r=a**b
	    t=sumdigit(r)
	    if t>max_sum:
		print a,b
		max_sum=t

    print max_sum

solve()
