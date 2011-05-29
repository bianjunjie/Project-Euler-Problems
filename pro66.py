#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro66.py
# Description: 
import math
def issq(n):
    m=math.sqrt(n)
    m=int(m)
    return (m*m)==n


max_sq=-1
max_d=-1
for d in range(2,1001):
    if issq(d):
	continue
    y=1
    while True:
	n_sq=d*y*y+1
	if issq(n_sq):
	    print d,n_sq,math.sqrt(n_sq)
	    if math.sqrt(n_sq)>max_sq:
		max_sq=math.sqrt(n_sq)
		max_d=d
	    break
	y+=1
    

print max_sq,max_d



    
