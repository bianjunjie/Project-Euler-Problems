#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro47.py
# Description: 

import pro21
from prime import myprime
start=647

while True:
    l=[0]*4
    d=[0]*4
    for i in range(4):
#	print start+i
        d[i]=pro21.explode(start+i)
	if len(d[i].keys())==4:
	    l[i]=1
    if all(l):
	print start
	break
    start+=4

    
