#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro37.py
# Description: 

from prime import myprime

plist=myprime(1000000)
pdict={}
for p in plist:
    pdict[p]=1

plist=plist[4:]


s=0
index=0
for p in plist:
    q=p
    flag=True
    q=p/10
    while q>0:
	if not pdict.has_key(q):
	    flag=False
	    break
	q=q/10

    if not flag:
	continue

    i=1;q=-1;
    while q!=p:
	q=p%(10**(i))
	if not pdict.has_key(q):
	    flag=False
	    break
	i=i+1

    if not flag:
	continue
    index =index+1
    s += p
    print p
    if index==11:
	break

print s
