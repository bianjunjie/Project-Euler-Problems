#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro76.py
# Description: 

import psyco;
psyco.full()
from datetime import *


ans=[ [-1 for i in range(120)] for j in range(120) ]
def expand(num, m):
    s=[]
    if num<m:
	s.append([])
	return s
    if num<m*2 and num>=m:
	s.append([num])
	return s

    s.append([num])
    for i in range(m,int(num/2)+1):
	t=expand(num-i, i)
	for _t in t:
	    s.append([i]+_t)
    return s



def expand2(num,m):
    global ans
    if ans[num][m]!=-1:
	return ans[num][m]

    s=0
    if num<m:
	ans[num][m]=0
	return 0
    if num<m*2 and num>=m:
	ans[num][m]=1
	return 1


    s+=1
    for i in range(m,int(num/2)+1):
	t=expand2(num-i, i)
	s+=t

    ans[num][m]=s
    return s

t1=datetime.now()
s=expand(45,1)
print len(s)-1
print datetime.now()-t1


t1=datetime.now()
s2=expand2(100,1)
print s2-1
print datetime.now()-t1
