#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro26.py
# Description: 

def cycle(num):
    remain=[1]

    t=1
    while(True):
	t*=10
	if (t%num==0):
	    return 0
	t-= (t/num)*num
	
	if t in remain:
	    #print num,remain,t
	    return len(remain)-remain.index(t)+1
	remain.append(t)
    return

imax=-1
for i in range(2,1000):
    if cycle(i) > imax:
	imax=cycle(i)

print imax
