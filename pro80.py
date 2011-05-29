#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro80.py
# Description: 

import math

def issq(num):
    if int(math.sqrt(num))**2  == num:
	return True
    return False

def calroot(num,r, length=100):
    base=int(math.sqrt(num))
    if base>=10:
	r.append(base/10)
	r.append(base%10)
    else:
	r.append(base)

    while True:
	if len(r)==length:
	    return 

	base=base*10
	num=num*100
	for k in range(9,-1, -1):
	    if (base+k)**2<=num:
		r.append(k)
		base+=k
		break
    return 

s=0
for i in range(1,101):
    r=[]
    if not issq(i):
	calroot(i,r,100)
	s+=sum(r)
print s

    

    

