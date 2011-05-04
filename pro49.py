#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro49.py
# Description: 


from copy import copy
from prime import myprime

def num2list(num):
    listNum=[int(i) for i in str(num)]
    return listNum

def list2num(l):
    n=0
    for i in l:
	n=n*10+i
    return n

def permutation(numStr):
    if len(numStr)==1:
	return [numStr]
    l=list(numStr)

    P=[]
    for i in l:
	T=copy(l)
	T.remove(i)
	newNumStr=''.join(T)
	rs=permutation(newNumStr)
	for r in rs:
	    P.append(i+r)
    return P


plist=myprime(10000)
pdict={}
for p in plist:
    pdict[p]=1
for p in plist:
    if p<1000:
	continue
    if not pdict.has_key(p):
	continue

    ps=permutation(str(p))
    ps=[int(pp) for pp in ps]
    ps=list(set(ps))
    ps=[i for i in ps if pdict.has_key(i) and i>1000]
   # print ps
    
    for p3 in ps:
	for p2 in ps:
	    for p1 in ps:
		if (p1+p3)==p2*2 and p3>p2 and p2>p1:
		    print p1,p2,p3
    
    for pp in ps:
	if pdict.has_key(pp):
	    del pdict[pp]
    
