#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro21.py
# Description: 

import prime

p=prime.myprime(1000000)

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



def sumup(num):
    d=explode(num)
    s=1
    for k in d.keys():
	s=s*(1- k**(d[k]+1))/(1-k)
    s-=num
    return s

if __name__=='__main__':
    mysum=0
    for i in range(2,10000):
	j=sumup(i)
	if (j<10000 and j>i and sumup(j)==i):
	    mysum+=(i+j)
	    print i,j

    print mysum

