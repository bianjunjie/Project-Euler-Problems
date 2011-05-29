#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro62.py
# Description: 

import math

def transTostr(num):
    s=[0]*10
    t=[]
    while num>0:
	s[num%10]+=1
	num/=10
    for i in s:
	if i>=10:
	    t.append(str(i))
	else:
	    t.append('0'+str(i))
    return ''.join(t)

custart=1e7
cuend=1e8-1

found=False
while True:
    start=math.ceil(custart**(1.0/3))
    end  =math.floor(cuend**(1.0/3))

    d={}
    ans={}
    for i in range(int(start), int(end)+1):
	cui=i**3
	str_cui=transTostr(cui)
	d[str_cui]=d.get(str_cui,0)+1
	if ans.has_key(str_cui):
	    ans[str_cui].append(i)
	else:
	    ans[str_cui]=[i]

    for k in d.keys():
	if d[k]==5:
	    print ans[k]
	    found=True
    if found:
	break
    custart*=10
    cuend=(cuend+1)*10-1
