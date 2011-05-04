#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro23_2.py
# Description: 

def isAbd(num):
    s=0
    for i in xrange(1,num):
	if (num%i==0):
	    s+=i
    if s>num:
	return True
    return False

numbers=range(28124)
del numbers[0]
abd=[]

for i in numbers:
    if isAbd(i):
	abd.append(i)

print len(abd)


