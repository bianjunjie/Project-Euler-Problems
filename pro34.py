#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro34.py
# Description: 



def sumFact(num):
    product=[1,1,2,6,24,120,720,5040,40320,362880]
    s=0
    while num>0 :
	s += product[num%10]
	num/=10
    return s

s=0
print sumFact(145)
for num in xrange(10,1000000):
    if num==sumFact(num):
	s+=num

print s


