#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro50.py
# Description: 

import prime
plist=prime.myprime(1000000)
plen =len(plist)
pdict={}
for p in plist:
    pdict[p]=1


s=[0]*(plen+1)
s[0]=0
s[1]=plist[0]
for i in range(2,plen):
    s[i]=s[i-1]+plist[i-1]



def binsearch(start, end, MAX, s):
    st=start
    en=end
    if s[en]-s[st] <=MAX:
	return en
    while en>=st:
	mid=(en+st)/2
	if s[mid]-s[st] >MAX:
	    en=mid-1
	else:
	    if s[mid+1]-s[st] >MAX:
		return mid
	    else:
		st=mid+1
    return st
	    

MAX=1000000
start=0
end=plen;
maxLen=-1;
maxPrime=-1;
while True:
    bestIdx=binsearch(start,end,MAX,s)
    while bestIdx > start:
	num=s[bestIdx]-s[start]
	if pdict.has_key(num) and bestIdx-start >maxLen:
	    maxLen=bestIdx-start;
	    maxPrime=num
	    break
	if pdict.has_key(num)==1:
	    break
	bestIdx-=1
    start+=1
    if s[start+maxLen]-s[start] > MAX:
	break


print maxLen, maxPrime

    
	    

