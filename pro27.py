#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro27.py
# Description: 

import prime
import math

def isPrime(num):
    if (num<=1):
	return False
    if (num==2 or num==3 or num==5):
	return True
    if (num%2==0 or num%3==0 or num%5==0):
	return False

    sq=int(math.sqrt(num))

    i=3
    while i<=sq:
	if num%i==0:
	    return False
	i+=2
    return True
    
pb=prime.myprime(1000)

def myfunc(a,b,x):
    return x*x+a*x+b
def quad(a,b):
    n=0
    s=0
    while True:
	if not isPrime(myfunc(a,b,n)):
	    break
	n+=1
	s+=1
    return s



ia=0
ib=0
imax=-1
for a in range(-999,1000):
    for b in pb:
	tmp=quad(a,b)
	if imax<quad(a,b) :
	    imax=tmp
	    ia=a
	    ib=b

print ia*ib
	    

