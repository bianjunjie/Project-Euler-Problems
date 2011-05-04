#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro35.2.py
# Description: 

import prime

plist=prime.myprime(1000000)
pdict={}
for p in plist:
    pdict[p]=1

def circular(num):
    if len(str(num))==1:
	return [num]
    
    l=len(str(num))
    s_num=str(num)
    r=[num]
    for i in range(1,l):
	s_next= s_num[i:]+s_num[0:i]
	r.append(int(s_next))
    return r



s=set()
for p in plist:
    lp=circular(p)
    flag=True

    for l in lp:
	if not pdict.has_key(l):
	    flag=False
	    break

    if p==17:
	print lp,flag,pdict[17],pdict[71]
    if flag:
	s=s.union(set(lp))

print len(s)


	

