#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro50.py
# Description: 

import prime
plist=prime.myprime(1000000)
plen =len(plist)
'''
sump=[0]*(plen+1)
j=1
for i in plist:
    sump[j]=sump[j-1]+i
    j +=1


maxLen=21
maxP  =963
for (i,p) in enumerate(plist):
#    if p<953:
#	continue

    if i%100==0:
	print i
    for j in range(i-1,0,-1):
	for k in range(j-maxLen,0,-1):
	    if sump[j]-sump[k]==p:
		tmpLen=j-k
		if tmpLen>maxLen:
		    maxLen=tmpLen
		    maxP  =p
		    print maxLen,maxP
	    if sump[j]-sump[k]>p:
		break
print maxP,maxLen

'''

pdict={}
for p in plist:
    pdict[p]=1


sump=[0]*(plen+1)
j=1
for i in plist:
    sump[j]=sump[j-1]+i
    j +=1

maxLen=21

maxStart=0
idx=0
while True:
    span=maxLen
    while True:
	endidx=idx+span
	pnum=sump[endidx]-sump[idx]
	if pnum>1000000:
	    break
	if pdict.has_key(pnum):
	    maxLen=span
	    span+=1
	    maxStart=plist[idx]
	    print span,maxStart
	
    idx+=1
    if plist[idx]*maxLen>1000000:
	break

print maxLen, maxStart

