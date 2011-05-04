#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro21.py
# Description: 

import prime
from datetime import datetime

print datetime.now()
p=prime.myprime(30000)

def explode(num):
    d={}
    global p

    i=0
    while num!=1:
	if num % p[i]==0:
	    num/=p[i]
	    d[p[i]]=d.get(p[i],0)+1
	else:
	    i+=1
    return d

MAX_NUM=28123
def sumup(num):
    d=explode(num)
    s=1
    for k in d.keys():
	s=s*(1- k**(d[k]+1))/(1-k)
    s-=num
    return s


abtList=[0]*(MAX_NUM+1)
for num in range(MAX_NUM+1):
    if num<12:
	abtList[num]=0
    elif sumup(num)>num:
	abtList[num]=1
    else:
	abtList[num]=0



def isAboundant(num):
    if num>MAX_NUM:
	return True
    if abtList[num]:
	return True
    return False



def splitAboundant(num):
    if num>MAX_NUM:
	return True
    if num<24:
	return False

    for i in range(12,num/2+1):
	j=num-i
	if j<i:
	    continue
	if isAboundant(i) and isAboundant(j):
	    return True
    return False
s=0
for i in range(MAX_NUM+1):
    if not splitAboundant(i):
	s += i

print s

print datetime.now()
'''
abd=[]
for i in range(12,MAX_NUM):
    if sumup(i)>i:
	abd.append(i)


l=len(abd)

sk=[0]*(MAX_NUM+1)
for i in xrange(l):
    if i%500==0:
	print i
    for j in xrange(i,l):
	if i+j<=MAX_NUM:
	    sk[i+j]=1
	else:
	    break
	

s=0
for i in xrange(len(sk)):
    if sk[i]==0:
	s+=i
print s,sum(sk)
'''
