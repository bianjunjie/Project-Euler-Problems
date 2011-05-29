#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro99.py
# Description: 
import math

maxlog=-1
linenum=-1
k=0
for line in open('base_exp.txt').readlines():
    k+=1
    i=[float(j) for j in line.strip().split(',')]
    t=i[1]*math.log(i[0])
    if t>maxlog:
	maxlog=t
	linenum=k
print linenum,maxlog


