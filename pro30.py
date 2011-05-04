#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro30.py
# Description: 

def mypow(num, k):
    s=0
    while(num>0):
	last=num%10
	s+=last**k
	num/=10
    return s


s=0
for i in range(11,1000000):
    if i==mypow(i,5):
	s+=i

print s

