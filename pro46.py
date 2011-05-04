#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro46.py
# Description: 

import prime
import math

plist=prime.myprime(1000000)
pdict={}
for p in plist:
    pdict[p]=1


num=33
while True:
    num=num+2
    if pdict.has_key(num):
	continue

    
    t=int(math.sqrt(num/2))

    flag=False
    for i in range(t+1):
	p=num-2*i*i
	if pdict.has_key(p):
	    flag=True
	    print '%d = %d + 2*%d*%d',(num,p,i,i)
	    break

    if flag==False:
	print num
	break




