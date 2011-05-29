#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro91.py
# Description: 

from datetime import datetime

t1=datetime.now()
m=50;n=50
s=0
for i in range(0,m+1):
    for j in range(0,n+1):
	for k in range(0,m+1):
	    for l in range(0,n+1):
		if k==i and l==j:
		    continue
		if i==0 and j==0:
		    continue
		if k==0 and l==0:
		    continue
		x1=i;y1=j
		x2=k;y2=l
		if y1*x2==y2*x1:
		    continue

		side=[]
		side.append(x1**2+y1**2)
		side.append(x2**2+y2**2)
		side.append((x1-x2)**2+(y1-y2)**2)
		side=sorted(side)
#		print side
		if side[0]+side[1]==side[2]:
		    s+=1

print s/2
print  datetime.now()-t1
